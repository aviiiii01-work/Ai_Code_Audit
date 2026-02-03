# Local GGUF LLM — FastAPI + llama.cpp (CPU)

A fully local, CPU-only LLM chat system using **GGUF models**, **llama.cpp**, **FastAPI**, and **Streamlit UI**. This project focuses on **deterministic behavior**, **low hallucination**, and **production-grade fixes** for common local-LLM issues (identity confusion, role echoing, UI glitches).

---

## Features

* Fully **offline / local** inference (GGUF)
* **FastAPI** backend for inference
* **Streamlit** chat UI
* CPU-only (no CUDA required)
* Strong **system prompt constraints**
* Output sanitization (role / name echo removal)
* Deterministic responses (low temperature)
* Clean chat history rendering (no hidden last message)

---

## Architecture Overview

```
ui/ (Streamlit)
  └── app.py
        ↓ REST
api/ (FastAPI)
  └── chat.py
        ↓
llama.cpp (CPU)
  └── GGUF Model

config/
  └── config.py
utils/
  └── sanitize.py
```

---

## Project Structure

```
project-root/
│
├── api/
│   └── chat.py
├── ui/
│   └── app.py
├── utils/
│   └── sanitize.py
├── deploy/
│   └── config.py
├── quantized/
│   └── model.gguf
├── README.md
└── final-report.md
```

---

## Configuration

All critical runtime parameters are defined in:

`deploy/config.py`

* Context size (`n_ctx`)
* CPU threads (`n_threads`)
* Generation parameters (temperature, top_p, top_k)
* Strict **SYSTEM_PROMPT** rules to prevent identity adoption

---

## Key Problems Solved

| Problem                   | Status  |
| ------------------------- | ------- |
| Identity hallucination    | Fixed |
| Role/name echo ("Ravi:")  | Fixed |
| Model claiming to be user | Fixed |
| Last message hidden in UI | Fixed |
| Over-random responses     | Fixed |

---

##  How to Run

### 1 Install dependencies

```
pip install -r requirements.txt
```

### 2 Start FastAPI backend

```
uvicorn deploy.app:app --host 0.0.0.0 --port 8000
```

### 3 Start Streamlit UI

```
streamlit run ui/app.py
```

---

##  Design Philosophy

* **Post-processing over prompt hacks**
* **Determinism over creativity**
* **Fail-safe defaults**
* **No hidden memory claims**

This project is meant to behave like a **reliable local assistant**, not a role-playing chatbot.

---

##  Future Improvements

* Stop-token enforcement in llama.cpp
* Conversation window pruning
* Multi-agent orchestration
* Tool-using agents
* Persistent vector memory (optional)

---

##  Author

**Ravi Pratap Singh**
Software Engineer | AI / ML | Local LLM Systems

---

##  License

MIT License
