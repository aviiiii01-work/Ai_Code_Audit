import torch
import clip
import numpy as np
from PIL import Image

class CLIPEmbedder:
    def __init__(self, model_name="ViT-B/32", device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model, self.preprocess = clip.load(model_name, device=self.device)

    def embed_text(self, texts):
        tokens = clip.tokenize(texts).to(self.device)
        with torch.no_grad():
            embeddings = self.model.encode_text(tokens)
        embeddings = embeddings / embeddings.norm(dim=-1, keepdim=True)
        return embeddings.cpu().numpy()

    def embed_image(self, image_path):
        image = Image.open(image_path).convert("RGB")
        image = self.preprocess(image).unsqueeze(0).to(self.device)
        with torch.no_grad():
            embedding = self.model.encode_image(image)
        embedding = embedding / embedding.norm(dim=-1, keepdim=True)
        return embedding.cpu().numpy()
