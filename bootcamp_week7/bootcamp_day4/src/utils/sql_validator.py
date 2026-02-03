FORBIDDEN_KEYWORDS = [
    "drop",
    "delete",
    "truncate",
    "update",
    "insert",
    "alter",
    ";",
    "--"
]

def validate_sql(sql: str):
    sql_lower = sql.lower().strip()

    if not sql_lower.startswith("select"):
        raise ValueError("Only SELECT queries are allowed")

    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in sql_lower:
            raise ValueError(f"Forbidden SQL keyword detected: {keyword}")

    return True
