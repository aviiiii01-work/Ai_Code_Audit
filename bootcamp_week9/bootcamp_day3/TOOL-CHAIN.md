# TOOL-CHAIN: DAY 3 Deliverables

## System Design
An **Autonomous Multi-Agent System** using **AutoGen v0.4** that bridges natural language to local system execution. It uses a single **Orchestrator Agent** with a dynamic "Tool Belt" to select tools based on user intent.

## Agent Toolset

| Tool | Function | Purpose |
| :--- | :--- | :--- |
| **DB Agent** | `run_postgresql_query` | Executes SQL on PostgreSQL `people_db`. Handles DATE-to-String conversion. |
| **Code Agent** | `execute_python_logic` | Runs dynamic Python scripts via `exec()` and returns printed output. |
| **File Agent** | `read_or_write_file` | Handles local I/O (Read/Write) for `.py`, `.csv`, and `.txt` files. |

## Execution Logic
1.  **Intent Analysis:** LLM parses the request (e.g., "Query DB and save").
2.  **Sequential Chaining:** Disables parallel calling to ensure **Tool A (DB)** returns real data before **Tool B (File)** is invoked.
3.  **Reflection:** The agent reviews the output of each tool call before deciding to proceed or **TERMINATE**.

## Key Features
* **Model:** Local Mistral-7B via Ollama (OpenAI-Compatible API).
* **Safety:** Sequential execution prevents variable hallucination (e.g., saving `$RESULT` instead of actual data).
* **Autonomy:** The agent ignores unnecessary tools (e.g., skips DB agent for pure math tasks).