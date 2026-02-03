# Agent Memory System Documentation

## Architecture Overview
This system implements a three-tier memory architecture for autonomous agents using the AutoGen 0.4+ framework.

### 1. Short-Term Memory (Session)
- **Location:** `/memory/session_memory.py`
- **Implementation:** RAM-based Sliding Window (Python `deque`).
- **Function:** Maintains the immediate conversation flow.

### 2. Semantic Memory (Vector Store)
- **Location:** `/memory/vector_store.py`
- **Implementation:** FAISS + SentenceTransformers (`all-MiniLM-L6-v2`).
- **Function:** Similarity-based recall. It embeds every user interaction and retrieves the top `k` most relevant past messages to provide context to the LLM.

### 3. Long-Term Memory (Persistent)
- **Location:** `/memory/long_term_db.py`
- **Implementation:** SQLite (`long_term.db`).
- **Function:** Stores hard facts (e.g., Project names, User IDs) that must survive system restarts. This is accessed via Agent Tool Calling.

## Execution Flow
1. **Query:** User sends a message.
2. **Retrieve:** System searches FAISS for similar past messages.
3. **Augment:** Relevant history is injected into the prompt as a `UserMessage` hint.
4. **Tool Use:** If the user specifies a fact to "register," the agent triggers the SQLite tool.
5. **Generate:** The LLM generates a response informed by both recent and distant history.