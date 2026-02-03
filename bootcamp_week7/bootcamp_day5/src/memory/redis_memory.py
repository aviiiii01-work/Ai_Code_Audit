import json
import redis
from typing import List, Dict, Any


class RedisMemory:
    def __init__(
        self,
        host: str = "localhost",
        port: int = 6379,
        db: int = 0,
        max_messages: int = 5,
        ttl: int = 1800
    ):
        self.client = redis.Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=True
        )
        self.max_messages = max_messages
        self.ttl = ttl

    def _key(self, session_id: str) -> str:
        return f"chat_memory:{session_id}"


    def add_message(self, session_id: str, role: str, content: str) -> None:
        key = self._key(session_id)

        message = json.dumps({
            "role": role,
            "content": content
        })

        self.client.rpush(key, message)
        self.client.ltrim(key, -self.max_messages, -1)
        self.client.expire(key, self.ttl)

    def get_messages(self, session_id: str) -> List[Dict]:
        key = self._key(session_id)
        messages = self.client.lrange(key, 0, -1)
        return [json.loads(m) for m in messages]

    def get_context(self, session_id: str) -> str:
        messages = self.get_messages(session_id)
        return "\n".join(
            f"{m['role']}: {m['content']}"
            for m in messages
        )


    def add_turn(
        self,
        session_id: str,
        question: str,
        answer: str,
        source: str
    ) -> None:
        key = self._key(session_id)

        turn = json.dumps({
            "question": question,
            "answer": answer,
            "source": source
        })

        self.client.rpush(key, turn)
        self.client.ltrim(key, -self.max_messages, -1)
        self.client.expire(key, self.ttl)

    def get_turns(self, session_id: str) -> List[Dict[str, Any]]:
        key = self._key(session_id)
        turns = self.client.lrange(key, 0, -1)
        return [json.loads(t) for t in turns]

    def get_turn_context(self, session_id: str) -> str:
        turns = self.get_turns(session_id)

        return "\n".join(
            f"Q: {t['question']}\nA: {t['answer']}"
            for t in turns
        )


    def clear(self, session_id: str) -> None:
        self.client.delete(self._key(session_id))
