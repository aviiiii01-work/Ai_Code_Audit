import time
import uuid
import re
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from deploy.model_loader import get_model
from deploy.config import GENERATION_DEFAULTS, SYSTEM_PROMPT

app = FastAPI(title="Local GGUF LLM API")


class GenerateRequest(BaseModel):
    prompt: str
    max_tokens: int | None = None
    temperature: float | None = None
    top_p: float | None = None
    top_k: int | None = None


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[ChatMessage]
    max_tokens: int | None = None
    temperature: float | None = None
    top_p: float | None = None
    top_k: int | None = None



def merge_params(req):
    params = GENERATION_DEFAULTS.copy()
    for k in params:
        val = getattr(req, k, None)
        if val is not None:
            params[k] = val
    return params


def build_chat_prompt(messages):
    prompt = f"System: {SYSTEM_PROMPT}\n\n"

    for msg in messages:
        role = "User" if msg.role == "user" else "Assistant"
        prompt += f"{role}: {msg.content}\n"

    prompt += "Assistant: "
    return prompt



def is_unknown_acronym(text: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z]{2,5}", text.strip()))


def last_user_message(messages: list[ChatMessage]) -> str | None:
    for msg in reversed(messages):
        if msg.role == "user":
            return msg.content
    return None



@app.post("/generate")
def generate(req: GenerateRequest):
    request_id = str(uuid.uuid4())
    llm = get_model()
    params = merge_params(req)

    if is_unknown_acronym(req.prompt):
        return {
            "request_id": request_id,
            "latency_sec": 0,
            "response": "I am not certain based on my knowledge."
        }

    prompt = (
        f"<system>\n{SYSTEM_PROMPT}\n</system>\n\n"
        f"<user>\n{req.prompt}\n</user>\n\n<assistant>\n"
    )

    start = time.time()
    output = llm(
        prompt,
        max_tokens=params["max_tokens"],
        temperature=params["temperature"],
        top_p=params["top_p"],
        top_k=params["top_k"],
    )
    latency = round(time.time() - start, 2)

    text = output["choices"][0]["text"].strip()

    return {
        "request_id": request_id,
        "latency_sec": latency,
        "response": text if text else "[No output generated]"
    }


@app.post("/chat")
def chat(req: ChatRequest):
    request_id = str(uuid.uuid4())
    llm = get_model()
    params = merge_params(req)

    last_msg = last_user_message(req.messages)
    if last_msg and is_unknown_acronym(last_msg):
        return StreamingResponse(
            iter(["I am not certain based on my knowledge."]),
            media_type="text/plain"
        )

    prompt = build_chat_prompt(req.messages)

    def token_stream():
        generated_any = False
        for out in llm(
            prompt,
            max_tokens=params["max_tokens"],
            temperature=params["temperature"],
            top_p=params["top_p"],
            top_k=params["top_k"],
            stream=True,
        ):
            token = out["choices"][0]["text"]
            if token:
                generated_any = True
                yield token

        if not generated_any:
            yield "\n[No response generated]"

    return StreamingResponse(token_stream(), media_type="text/plain")
