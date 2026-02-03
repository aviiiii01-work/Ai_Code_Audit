class SQLPromptGenerator:
    def __init__(self, schema_text: str):
        self.schema_text = schema_text

    def build_prompt(self, user_question: str) -> str:
        prompt = f"""
You are a PostgreSQL expert.

Given the database schema below, write ONLY a valid SQL query.
- Do NOT explain anything.
- Do NOT include markdown.
- Do NOT include comments.
- Return ONLY SQL.

Database Schema:
{self.schema_text}

User Question:
{user_question}

SQL Query:
"""
        return prompt.strip()
