import json
import numpy as np
from rank_bm25 import BM25Okapi


class HybridRetriever:
    def __init__(self, index, chunks, model):
        self.index = index
        self.chunks = chunks
        self.model = model

        self.texts = [chunk["text"] for chunk in chunks]
        tokenized = [text.lower().split() for text in self.texts]
        self.bm25 = BM25Okapi(tokenized)

    def semantic_search(self, query, top_k):
        query_vec = self.model.encode([query])
        distances, indices = self.index.search(query_vec, top_k)

        results = []
        for rank, idx in enumerate(indices[0]):
            chunk = self.chunks[idx].copy()
            chunk["score"] = float(distances[0][rank])
            chunk["retrieval"] = "semantic"
            results.append(chunk)

        return results

    def keyword_search(self, query, top_k):
        tokens = query.lower().split()
        scores = self.bm25.get_scores(tokens)
        ranked = np.argsort(scores)[::-1][:top_k]

        results = []
        for idx in ranked:
            if scores[idx] <= 0:
                continue
            chunk = self.chunks[idx].copy()
            chunk["score"] = float(scores[idx])
            chunk["retrieval"] = "keyword"
            results.append(chunk)

        return results

    def apply_filters(self, chunks, filters):
        if not filters:
            return chunks

        filtered = []
        for chunk in chunks:
            valid = True
            for key, value in filters.items():
                if chunk.get(key) != value:
                    valid = False
                    break
            if valid:
                filtered.append(chunk)

        return filtered

    def retrieve(self, query, top_k=5, filters=None):
        semantic = self.semantic_search(query, top_k)
        keyword = self.keyword_search(query, top_k)

        combined = semantic + keyword
        combined = self.apply_filters(combined, filters)

        seen = set()
        unique = []

        for chunk in combined:
            cid = chunk["chunk_id"]
            if cid not in seen:
                seen.add(cid)
                unique.append(chunk)

        return unique[:top_k]
