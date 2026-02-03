from sentence_transformers import CrossEncoder


class Reranker:
    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        self.model = CrossEncoder(model_name)

    def rerank(self, query: str, chunks: list, top_k: int = 5):
        if not chunks:
            return []

        sentence_pairs = []
        for chunk in chunks:
            sentence_pairs.append((query, chunk["text"]))

        scores = self.model.predict(sentence_pairs)

        for idx, chunk in enumerate(chunks):
            chunk["rerank_score"] = float(scores[idx])

        ranked_chunks = sorted(
            chunks,
            key=lambda x: x["rerank_score"],
            reverse=True
        )

        return ranked_chunks[:top_k]
