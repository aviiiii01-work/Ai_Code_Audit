import faiss
import pickle

class ImageRetriever:
    def __init__(self, index_path, metadata_path):
        self.index = faiss.read_index(index_path)
        with open(metadata_path, "rb") as f:
            self.metadata = pickle.load(f)

    def search(self, query, k=3):
        """
        FAISS index already stores vectors.
        We retrieve by text similarity through metadata ONLY.
        """
        query_lower = query.lower()

        scored = []
        for item in self.metadata:
            text = item.get("text", "").lower()
            score = sum(1 for w in query_lower.split() if w in text)
            if score > 0:
                scored.append((score, item))

        scored.sort(reverse=True, key=lambda x: x[0])
        return [item for _, item in scored[:k]]
