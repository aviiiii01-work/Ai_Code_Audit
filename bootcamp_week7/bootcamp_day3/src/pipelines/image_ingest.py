import os
import pytesseract
from PIL import Image
from src.embeddings.clip_embedder import CLIPEmbedder
from src.embeddings.blip_captioner import BLIPCaptioner
from src.retriever.image_retriever import ImageRetriever

class ImageIngest:
    def __init__(self, embedding_dim=512, device=None):
        self.clip = CLIPEmbedder(device=device)
        self.blip = BLIPCaptioner(device=device)
        self.retriever = ImageRetriever(embedding_dim)

    def process_folder(self, folder_path):
        print("Resetting existing index...")
        self.retriever.reset()
        for fname in os.listdir(folder_path):
            if not fname.lower().endswith((".png", ".jpg", ".jpeg")):
                continue

            image_path = os.path.join(folder_path, fname)
            image = Image.open(image_path).convert("RGB")

            ocr_text = pytesseract.image_to_string(image)
            caption = self.blip.generate_caption(image_path)
            img_embedding = self.clip.embed_image(image_path)

            self.retriever.add(
                embedding=img_embedding,
                meta={
                    "path": image_path,
                    "ocr": ocr_text.strip(),
                    "caption": caption
                }
            )

        self.retriever.save()
        print(f"Ingested {len(self.retriever.metadata)} images")
