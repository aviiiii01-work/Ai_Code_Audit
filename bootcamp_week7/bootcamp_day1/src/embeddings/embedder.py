import json
from pathlib import Path
import yaml
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

settings_path = Path(__file__).resolve().parents[1] / "config" / "settings.yaml"
with open(settings_path, "r") as f:
    config = yaml.safe_load(f)

CHUNKS_DIR = Path(config["data_paths"]["chunks"])
EMBEDDINGS_DIR = Path(config["data_paths"]["embeddings"])
VECTORSTORE_DIR = Path(config["data_paths"]["vectorstore"])

EMBEDDINGS_DIR.mkdir(parents=True, exist_ok=True)
VECTORSTORE_DIR.mkdir(parents=True, exist_ok=True)

chunks_file = CHUNKS_DIR / "chunks.jsonl"
chunks = []

with open(chunks_file, "r", encoding="utf-8") as f:
    for line in f:
        chunks.append(json.loads(line))

texts = [chunk["text"] for chunk in chunks]

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)

embeddings_file = EMBEDDINGS_DIR / "chunk_embeddings.npy"
np.save(embeddings_file, embeddings)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

faiss_index_file = VECTORSTORE_DIR / "index.faiss"
faiss.write_index(index, str(faiss_index_file))

print(f"Embeddings saved at: {embeddings_file}")
print(f"FAISS index saved at: {faiss_index_file}")

