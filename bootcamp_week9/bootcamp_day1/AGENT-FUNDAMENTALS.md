# AGENT-FUNDAMENTALS.md

## Message-Based Communication
The system uses the `on_messages` protocol to facilitate **Role Isolation**. 

### Reasoning Loop
1. **Perception**: The agent receives a `TextMessage`.
2. **Reasoning**: The internal `Mistral-7B` model processes the text against the `System Message`.
3. **Action**: The agent produces a `Response` containing a `chat_message`.

### Memory & State
Each agent maintains its own internal state. By passing the `content` of a message from one agent to the next, we maintain the chain of thought without bloating the local model's context window.