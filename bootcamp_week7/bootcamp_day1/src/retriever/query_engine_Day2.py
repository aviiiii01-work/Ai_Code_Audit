import json
import numpy as np
import faiss
from pathlib import Path
from sentence_transformers import SentenceTransformer
from bootcamp_week7.bootcamp_day1.src.retriever.hybrid_retriever_day2 import HybridRetriever
from bootcamp_week7.bootcamp_day1.src.retriever.reranker_day2 import Reranker
from bootcamp_week7.bootcamp_day1.src.pipelines.context_builder_day2 import build_context

BASE_DIR = Path(__file__).resolve().parents[2]

EMBEDDINGS_PATH = BASE_DIR / "src/data/embeddings/chunk_embeddings.npy"
INDEX_PATH = BASE_DIR / "src/data/vectorstore/index.faiss"
CHUNKS_PATH = BASE_DIR / "src/data/chunks/chunks.jsonl"

model = SentenceTransformer("all-MiniLM-L6-v2")

with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
    chunks = [json.loads(line) for line in f]

embeddings = np.load(EMBEDDINGS_PATH)
index = faiss.read_index(str(INDEX_PATH))

hybrid_retriever = HybridRetriever(
    index=index,
    chunks=chunks,
    model=model
)
reranker = Reranker()

def query_engine(query, top_k=5, filters=None):

    candidates = hybrid_retriever.retrieve(query, top_k=top_k, filters=filters)
    reranked = reranker.rerank(query, candidates)
    context = build_context(reranked)

    return context

if __name__ == "__main__":
    while True:
        user_query = input("Enter query: ").strip()
        if user_query.lower() in ["exit", "quit"]:
            print("Exiting Advanced Query Engine.")
            break
        top_context = query_engine(user_query, top_k=5, filters=None)
        print(top_context["context"])
        print(f"\nTotal tokens: {top_context['total_tokens']}")

