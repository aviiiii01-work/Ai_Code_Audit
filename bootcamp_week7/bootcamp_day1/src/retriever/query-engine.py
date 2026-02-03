import numpy as np
import faiss
import json
from pathlib import Path
from sentence_transformers import SentenceTransformer

BASE_DIR = Path(__file__).resolve().parents[2]

EMBEDDINGS_PATH = BASE_DIR / "src/data/embeddings/chunk_embeddings.npy"
INDEX_PATH = BASE_DIR / "src/data/vectorstore/index.faiss"
CHUNKS_PATH = BASE_DIR / "src/data/chunks/chunks.jsonl"

model = SentenceTransformer("all-MiniLM-L6-v2")

with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
    chunks = [json.loads(line) for line  in f]

embeddings = np.load(EMBEDDINGS_PATH)
index = faiss.read_index(str(INDEX_PATH))

def query_engine(query, top_k=5):
    query_vector = model.encode([query])
    distances, indices = index.search(query_vector, top_k)

    results = []
    for idx in indices[0]:
        results.append(chunks[idx])
    return results

if __name__ == "__main__":
    print("Welcome to the RAG Query Engine. Type 'exit' to quit.")
    while True:
        user_query = input("Enter query: ").strip()
        if user_query.lower() in ["exit", "quit"]:
            print("Exiting Query Engine.")
            break
        top_chunks = query_engine(user_query, top_k=5)
        print("\nTop results:\n")
        for chunk in top_chunks:
            print(chunk["text"])