from src.embeddings.clip_embedder import CLIPEmbedder

class ImageQueryEngine:
    def __init__(self, retriever, device=None):
        self.retriever = retriever
        self.clip = CLIPEmbedder(device=device)

    def text_to_image(self, query_text, top_k=5):
        query_embedding = self.clip.embed_text([query_text])
        return self.retriever.search(query_embedding, top_k)

    def image_to_image(self, query_image_path, top_k=5):
        query_embedding = self.clip.embed_image(query_image_path)
        return self.retriever.search(query_embedding, top_k)

    def image_to_text(self, query_image_path, top_k=5):
        results = self.image_to_image(query_image_path, top_k)
        return [
            {
                "path": r["path"],
                "ocr": r["ocr"],
                "caption": r["caption"]
            }
            for r in results
        ]
