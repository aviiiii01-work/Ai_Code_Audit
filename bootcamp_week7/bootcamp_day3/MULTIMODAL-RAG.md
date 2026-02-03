# MULTIMODAL-RAG (IMAGE-BASED RETRIEVAL AUGMENTED GENERATION)

## Project Overview
This project implements a **Multimodal Retrieval-Augmented Generation (RAG)** pipeline focused on **image understanding and retrieval**. The system ingests images, extracts visual and textual information, converts them into vector embeddings, stores them persistently, and supports multiple query modalities such as **text-to-image**, **image-to-image**, and **image-to-text** retrieval.

The goal of this implementation is to demonstrate how vision models, OCR, and vector databases can be combined to build a scalable multimodal retrieval system.

---
  
## Key Objectives
- Handle image data inside a RAG pipeline
- Generate and store image embeddings using vision-language models
- Extract text from images using OCR
- Generate semantic captions for images
- Perform similarity-based retrieval using FAISS
- Persist embeddings for reuse across multiple query sessions

---

## System Architecture
The system is divided into two clearly separated phases:

1. **Ingestion Phase (Run Once or Occasionally)**
2. **Query Phase (Run Multiple Times)**

This separation ensures efficiency and avoids recomputing embeddings repeatedly.

---

## Ingestion Pipeline
The ingestion pipeline processes a folder of images and performs the following steps for each image:

1. Load image from disk
2. Extract text using OCR (Tesseract)
3. Generate a descriptive caption using BLIP
4. Generate a dense vector embedding using CLIP
5. Store embeddings and metadata in a persistent FAISS index

### Stored Metadata Per Image
- Image file path
- OCR-extracted text
- BLIP-generated caption

The FAISS index and metadata are saved to disk, enabling persistent storage across sessions.

---

## Query Pipeline
Once ingestion is completed, the query pipeline loads the saved FAISS index and supports the following query modes:

### Text → Image
- Converts input text into a CLIP text embedding
- Retrieves visually and semantically similar images

### Image → Image
- Converts a query image into a CLIP image embedding
- Retrieves visually similar images from the dataset

### Image → Text
- Retrieves the most relevant image
- Returns its associated caption and OCR text

---

## Models and Tools Used
- **CLIP (ViT-B/32)**: For generating image and text embeddings
- **BLIP**: For image caption generation
- **Tesseract OCR**: For extracting text from images
- **FAISS**: For efficient similarity search and vector storage
- **PIL**: Image processing
- **PyTorch & Transformers**: Model execution

---

## Directory Structure
- src/
  - embeddings/
    - clip_embedder.py
    - blip_captioner.py
  - pipelines/
    - image_ingest.py
  - retriever/
    - image_retriever.py
  - query_engine/
    - image_query_engine.py
  - data/
    - images/        (dataset images)
    - query/         (query image)
  - ingest.py        (runs ingestion)
  - query.py         (runs queries)
- storage/
  - faiss.index
  - metadata.pkl

---

## Persistent FAISS Strategy
- Embeddings are generated **once**
- FAISS index and metadata are stored on disk
- Subsequent queries reuse the stored vectors
- Prevents recomputation and improves performance

To re-ingest from scratch, the storage directory can be cleared manually.

---

## Example Usage
1. Run ingestion to process images and store embeddings
2. Run query commands from the terminal to retrieve results
3. Use text or image inputs to explore the image dataset

---

## Key Learning Outcomes
- Understanding multimodal embeddings
- Designing persistent vector databases
- Applying OCR and image captioning in real-world pipelines
- Building scalable image-based retrieval systems
- Structuring ML pipelines for clarity and reuse

---

## Conclusion
This project demonstrates a complete and professional **Multimodal RAG pipeline** using modern vision-language models. It lays a strong foundation for extending into advanced use cases such as LLM-based reasoning, visual question answering, or multimodal chat systems.

The implementation follows best practices for modularity, persistence, and real-world applicability.
