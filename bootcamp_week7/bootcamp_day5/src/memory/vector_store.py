import os
import faiss
import pickle
import numpy as np
from typing import List, Dict
from sentence_transformers import SentenceTransformer


class VectorStore:
    def __init__(
        self,
        embedding_model: str = "all-MiniLM-L6-v2",
        dim: int = 384,
        index_path: str = "src/storage/faiss.index",
        meta_path: str = "src/storage/metadata.pkl"
    ):
        self.dim = dim
        self.index_path = index_path
        self.meta_path = meta_path

        self.model = SentenceTransformer(embedding_model)

        if os.path.exists(index_path) and os.path.exists(meta_path):
            self.index = faiss.read_index(index_path)
            with open(meta_path, "rb") as f:
                self.metadata = pickle.load(f)
        else:
            self.index = faiss.IndexFlatL2(dim)
            self.metadata = []

    def _embed(self, texts: List[str]) -> np.ndarray:
        embeddings = self.model.encode(texts, normalize_embeddings=True)
        return np.array(embeddings).astype("float32")

    def add(self, texts: List[str], metadatas: List[Dict]) -> None:
        assert len(texts) == len(metadatas)

        enriched_metadata = []
        for text, meta in zip(texts, metadatas):
            meta["text"] = text
            enriched_metadata.append(meta)

        embeddings = self._embed(texts)
        self.index.add(embeddings)
        self.metadata.extend(enriched_metadata)

        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "wb") as f:
            pickle.dump(self.metadata, f)

    def search(self, query: str, k: int = 3):
        query_embedding = self._embed([query])
        _, indices = self.index.search(query_embedding, k)

        seen = set()
        results = []

        for idx in indices[0]:
            if idx < len(self.metadata):
                text = self.metadata[idx]["text"]
                if text not in seen:
                    seen.add(text)
                    results.append(self.metadata[idx])

        return results

