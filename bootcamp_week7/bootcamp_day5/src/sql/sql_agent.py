ALLOWED_COLUMNS = [
    "id", "user_id", "first_name", "last_name", "sex",
    "email", "phone", "date_of_birth", "job_title"
]

class SQLAgent:
    def __init__(self, llm):
        self.llm = llm

    def generate_sql(self, question: str) -> str:
        prompt = f"""
You are a PostgreSQL expert.

Table name: people
Columns: {", ".join(ALLOWED_COLUMNS)}

Rules:
- Generate ONLY ONE SQL query
- ONLY SELECT queries
- No INSERT, UPDATE, DELETE, DROP
- No explanations, only SQL
- When filtering by text values, use LOWER(column) and lowercase literals

Question:
{question}
"""

        sql = self.llm.generate(prompt)
        return self._sanitize(sql)

    def _sanitize(self, sql: str) -> str:
        sql = sql.strip().lower()

        if not sql.startswith("select"):
            raise ValueError("Only SELECT queries allowed")

        forbidden = ["insert", "update", "delete", "drop", "alter"]
        if any(word in sql for word in forbidden):
            raise ValueError("Unsafe SQL detected")

        return sql
