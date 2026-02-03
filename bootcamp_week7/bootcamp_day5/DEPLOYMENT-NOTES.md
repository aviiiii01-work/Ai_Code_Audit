# DEPLOYMENT-NOTES.md

## Project: Advanced RAG Capstone
Bootcamp Week 7 – Day 5  
Author: Ravi Pratap Singh

---

## 1. Overview

This project is a multi-modal Retrieval-Augmented Generation (RAG) system exposed via FastAPI.  
It supports:
- Text-based RAG
- Image-based RAG (FAISS + embeddings)
- SQL-based question answering

Each API includes:
- Retrieval
- Answer generation
- Evaluation (faithfulness, confidence, hallucination)
- Custom threshold enforcement

The project is **not production-oriented** and is intended for learning, architecture validation, and evaluation experiments.

---

## 2. Tech Stack

- Python 3.12
- FastAPI
- Uvicorn
- FAISS
- Redis
- Ollama (local LLM + embeddings)
- Mistral model
- NumPy
- Pydantic

---

## 3. Directory Structure (Relevant)

bootcamp_week7/
└── bootcamp_day5/
    ├── src/
    │   ├── deployment/
    │   │   └── app.py
    │   ├── evaluation/
    │   │   ├── rag_eval.py
    │   │   └── thresholds.py
    │   ├── vector_store/
    │   │   └── image_retriever.py
    │   ├── query_engine/
    │   │   └── image_query_engine.py
    │   ├── memory/
    │   │   ├── redis_memory.py
    │   │   └── vector_store.py
    │   ├── llm/
    │   │   └── mistral_client.py
    │   └── sql/
    │       ├── sql_agent.py
    │       └── sql_executor.py
    └── venv/

FAISS storage:
bootcamp_week7/bootcamp_day3/storage/
- faiss.index
- metadata.pkl

---

## 4. Prerequisites

System:
- Linux / macOS
- Python 3.12+
- Minimum 8GB RAM

Services:
- Ollama (running locally)
- Redis (running locally)

---

## 5. Environment Setup

Create virtual environment:
python3 -m venv venv  
source venv/bin/activate  

Install dependencies:
pip install -r requirements.txt

---

## 6. Ollama Setup

Start Ollama:
ollama serve  

Pull model:
ollama pull mistral  

Endpoints used:
- Text generation: http://localhost:11434/api/generate
- Embeddings: http://localhost:11434/api/embeddings

---

## 7. Redis Setup

Start Redis:
redis-server  

Redis is used for:
- Session memory
- Conversation context persistence

---

## 8. FAISS Index Requirement (Critical)

The embedding model used during FAISS index creation **must match** the embedding model used during query time.

Mismatch results in:
AssertionError: assert d == self.d

Ensure:
- Same embedding model (mistral)
- Same embedding endpoint
- Same vector dimensionality

---

## 9. Running the Application

From bootcamp_day5 directory:

uvicorn src.deployment.app:app --reload  

Application URL:
http://127.0.0.1:8000  

Swagger UI:
http://127.0.0.1:8000/docs  

---

## 10. API Endpoints

### /ask — Text RAG

Purpose:
- Vector retrieval
- Context-grounded answer
- RAG evaluation + thresholds

Input:
{
  "question": "What is Retrieval Augmented Generation?",
  "session_id": "test-session-1"
}

---

### /ask-image — Image RAG

Purpose:
- FAISS-based retrieval
- Image metadata grounding
- Hallucination detection if no context

Input:
{
  "question": "What does the electrical circuit diagram represent?",
  "session_id": "image-test-1"
}

---

### /ask-sql — SQL RAG

Purpose:
- Question → SQL
- Query execution
- SQL-specific evaluation

Input:
{
  "question": "List all users with job title Engineer"
}

---

## 11. Evaluation Architecture

Metrics:
- context_match
- faithfulness
- confidence
- hallucinated

Threshold-based enforcement:
- /ask → THRESHOLDS["ask"]
- /ask-sql → THRESHOLDS["ask_sql"]
- /ask-image → default RAG evaluation

Hallucination is flagged explicitly in API response.

---

## 12. Logging

Text RAG interactions are logged to:
CHAT-LOGS.json

Each entry includes:
- timestamp
- session_id
- question
- answer
- evaluation

---

## 13. Known Limitations

- Not production-ready
- Image RAG depends on metadata quality
- SQL safety depends on SQLAgent constraints
- No authentication
- No rate limiting

---

## 14. Deployment Intent

Designed for:
- Local development
- Bootcamp evaluation
- RAG architecture demonstration
- Evaluation experimentation

Not designed for:
- Public internet deployment
- High concurrency
- Sensitive data handling

---

## 15. Status

Deployment verified  
APIs functional  
Evaluation integrated  
Swagger tested  

Day 5 Task: COMPLETED
