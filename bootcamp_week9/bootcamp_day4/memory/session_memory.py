from collections import deque
from typing import List, Dict

class SessionMemory:
    def __init__(self, max_messages: int = 10):
        """
        Initializes RAM-based short-term memory.
        :param max_messages: The maximum number of recent messages to keep.
        """
        self.history = deque(maxlen=max_messages)

    def add_message(self, role: str, content: str):
        """Adds a message turn to the short-term session."""
        self.history.append({"role": role, "content": content})

    def get_history(self) -> List[Dict[str, str]]:
        """Returns the current sliding window of conversation."""
        return list(self.history)

    def clear(self):
        """Wipes the current session (RAM only)."""
        self.history.clear()

    def format_for_prompt(self) -> str:
        """Returns history as a string to be injected into a prompt."""
        return "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in self.history])