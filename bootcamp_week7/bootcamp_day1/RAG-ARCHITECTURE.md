# Retrieval Augmented Generation (RAG) – Architecture Overview

## 1. What This Project Is
This project implements a **local, enterprise-style RAG (Retrieval Augmented Generation) system**.  
The goal is to answer user queries by grounding a language model on **private documents** instead of relying only on pretrained knowledge.

The system follows a **modular, production-oriented design**, similar to real-world GenAI systems used in companies for internal knowledge bases, documentation search, and AI assistants.

---

## 2. High-Level Architecture

The RAG system is divided into **five major stages**:

1. Data Ingestion  
2. Chunking & Preprocessing  
3. Embedding Generation  
4. Vector Storage & Retrieval  
5. Query Engine (Generation-ready)

Each stage is isolated so it can be modified, scaled, or replaced independently.

---

## 3. Directory-Level Architecture

src/
- config/        → Centralized YAML-based configuration
- data/
  - raw/          → Original documents (PDF, TXT, DOCX, CSV)
  - chunks/       → Chunked text stored as JSONL
  - embeddings/   → Numpy embedding arrays
  - vectorstore/  → FAISS index
- pipelines/     → Ingestion & preprocessing pipelines
- embeddings/    → Embedding generation logic
- retriever/     → Query engine (vector search)
- generator/     → Response generation (Day-2)
- prompts/       → Prompt templates (Day-2)
- utils/         → Shared helpers
- logs/          → Logging outputs

---

## 4. Stage 1 – Data Ingestion

**Purpose**  
Convert raw documents into structured text chunks.

**Input**
- PDF
- TXT
- DOCX
- CSV

**Output**
- JSONL file containing cleaned, chunked text

**Key Responsibilities**
- File type detection
- Text extraction
- Basic text cleaning
- Metadata attachment (source file, section id, chunk id)

**Why this matters**  
LLMs cannot process large documents directly. Ingestion ensures the data is usable by downstream components.

---

## 5. Stage 2 – Chunking Strategy

**Chunk Size**
- Default: ~700 characters

**Overlap**
- Default: ~100 characters

**Reasoning**
- Preserves semantic continuity
- Prevents loss of context at chunk boundaries
- Improves retrieval accuracy

Chunking is intentionally kept **simple and deterministic** for transparency and debuggability.

---

## 6. Stage 3 – Embedding Generation

**Model Used**
- sentence-transformers / all-MiniLM-L6-v2

**Process**
- Read chunked text
- Convert each chunk into a dense vector
- Store embeddings as NumPy arrays

**Why embeddings**
- Capture semantic meaning
- Allow similarity-based search
- Enable vector database indexing

---

## 7. Stage 4 – Vector Store (FAISS)

**Vector Database**
- FAISS (Facebook AI Similarity Search)

**Responsibilities**
- Store embeddings efficiently
- Perform fast nearest-neighbor search
- Return top-K most relevant chunks

**Why FAISS**
- Lightweight
- Fast
- Local-first (no external services)
- Industry-accepted for research and enterprise prototypes

---

## 8. Stage 5 – Query Engine (Retriever)

**Role**
Acts as the **retrieval layer** of the RAG system.

**Responsibilities**
- Accept user query
- Embed the query
- Search FAISS index
- Return top-K relevant chunks

This layer is intentionally **generation-agnostic**, making it reusable across:
- CLI tools
- APIs
- Chat interfaces
- Evaluation pipelines

---

## 9. Configuration-Driven Design

All system behavior is controlled via `settings.yaml`:
- Data paths
- Chunk size & overlap
- Retrieval parameters
- Logging level

**Benefits**
- No hardcoded values
- Environment flexibility
- Reviewer-friendly and production-ready

---

## 10. Why This Architecture Is Enterprise-Ready

- Clear separation of concerns
- Replaceable components
- Local-first, privacy-friendly
- Easy to extend with:
  - Rerankers
  - Hybrid search
  - LLM generators
  - APIs

This mirrors how real GenAI systems are built in production.

---

## 11. Current Status (End of Day-1)

Completed:
- Ingestion pipeline
- Chunking
- Embeddings
- Vector store
- Retrieval (Query Engine)

---
