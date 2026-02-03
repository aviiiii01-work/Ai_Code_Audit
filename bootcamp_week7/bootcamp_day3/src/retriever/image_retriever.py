import faiss
import numpy as np
import os
import pickle

class ImageRetriever:
    def __init__(self, embedding_dim, index_path="storage/faiss.index", meta_path="storage/metadata.pkl"):
        self.embedding_dim = embedding_dim
        self.index_path = index_path
        self.meta_path = meta_path

        if os.path.exists(index_path) and os.path.exists(meta_path):
            self.index = faiss.read_index(index_path)
            with open(meta_path, "rb") as f:
                self.metadata = pickle.load(f)

            if self.index.ntotal != len(self.metadata):
                print(f"WARNING: Index size ({self.index.ntotal}) != metadata size ({len(self.metadata)}). Resetting index.")
                self.index = faiss.IndexFlatIP(embedding_dim)
                self.metadata = []
        else:
            self.index = faiss.IndexFlatIP(embedding_dim)
            self.metadata = []

    def add(self, embedding, meta):
        embedding = np.asarray(embedding, dtype="float32")

        if embedding.ndim == 1:
            embedding = embedding.reshape(1, -1)

        self.index.add(embedding)
        self.metadata.append(meta)

    def save(self):
        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "wb") as f:
            pickle.dump(self.metadata, f)

    def reset(self):
        self.index = faiss.IndexFlatIP(self.embedding_dim)
        self.metadata = []


    def search(self, query_embedding, top_k=5):
        query_embedding = np.asarray(query_embedding, dtype="float32")

        if query_embedding.ndim == 1:
            query_embedding = query_embedding.reshape(1, -1)

        scores, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx in indices[0]:
            if idx == -1:
                continue
            if idx >= len(self.metadata):
                continue
            results.append(self.metadata[idx])

        return results
