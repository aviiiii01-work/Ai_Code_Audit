import json
import uuid
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
import requests

from src.memory.redis_memory import RedisMemory
from src.memory.vector_store import VectorStore

from src.evaluation.rag_eval import (
    evaluate_answer,
    apply_thresholds,
    SQLRAGEvaluator
)
from src.evaluation.thresholds import THRESHOLDS

from src.query_engine.image_query_engine import ImageQueryEngine
from src.vector_store.image_retriever import ImageRetriever

from src.llm.mistral_client import MistralLLM
from src.sql.sql_agent import SQLAgent
from src.sql.sql_executor import SQLExecutor


llm = MistralLLM()
sql_agent = SQLAgent(llm)
sql_executor = SQLExecutor()
sql_evaluator = SQLRAGEvaluator()

app = FastAPI(title="Advanced RAG Capstone")

memory = RedisMemory()
vector_store = VectorStore()

LOG_FILE = "CHAT-LOGS.json"
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"

BASE_DIR = Path(__file__).resolve().parents[3]
index_path = BASE_DIR / "bootcamp_day3/storage/faiss.index"
metadata_path = BASE_DIR / "bootcamp_day3/storage/metadata.pkl"

image_retriever = ImageRetriever(str(index_path), str(metadata_path))
image_engine = ImageQueryEngine(image_retriever, llm)


class AskRequest(BaseModel):
    question: str
    session_id: str | None = None


def call_llm(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload, timeout=60)
    return response.json()["response"]


def log_interaction(data: dict):
    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(data)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)


@app.post("/ask")
def ask(req: AskRequest):
    session_id = req.session_id or str(uuid.uuid4())

    chat_context = memory.get_context(session_id)

    retrieved = vector_store.search(req.question, k=3)
    contexts = [meta.get("text", str(meta)) for meta in retrieved]

    prompt = f"""
You are a factual assistant.

Conversation History:
{chat_context}

Retrieved Context:
{"\n".join(contexts)}

Question:
{req.question}

Answer using ONLY the retrieved context.
If not present, say "I don't know".
"""

    answer = call_llm(prompt)

    evaluation = evaluate_answer(answer, contexts)
    evaluation = apply_thresholds(evaluation, THRESHOLDS["ask"])

    memory.add_message(session_id, "user", req.question)
    memory.add_message(session_id, "assistant", answer)

    log_interaction({
        "timestamp": datetime.now().isoformat(),
        "session_id": session_id,
        "question": req.question,
        "answer": answer,
        "evaluation": evaluation
    })

    return {
        "session_id": session_id,
        "answer": answer,
        "evaluation": evaluation
    }


@app.post("/ask-image")
def ask_image(req: AskRequest):
    question = req.question
    session_id = req.session_id or "default"

    answer, contexts = image_engine.query(question)

    evaluation = evaluate_answer(answer, contexts)
    evaluation = apply_thresholds(evaluation, THRESHOLDS["ask_image"])

    memory.add_message(session_id, "user", question)
    memory.add_message(session_id, "assistant", answer)

    return {
        "question": question,
        "answer": answer,
        "contexts": contexts,
        "evaluation": evaluation,
        "source": "image"
    }


@app.post("/ask-sql")
def ask_sql(payload: dict):
    question = payload["question"]

    sql = sql_agent.generate_sql(question)
    columns, rows = sql_executor.run(sql)

    evaluation = sql_evaluator.evaluate(sql, rows)
    evaluation = apply_thresholds(evaluation, THRESHOLDS["ask_sql"])

    return {
        "question": question,
        "sql": sql,
        "rows": rows,
        "row_count": len(rows),
        "evaluation": evaluation
    }
