def extract_sql(text: str) -> str:
    lines = text.strip().splitlines()

    sql_lines = []
    for line in lines:
        if line.strip().lower().startswith("select"):
            sql_lines.append(line)
        elif sql_lines:
            sql_lines.append(line)

    sql = " ".join(sql_lines).strip()

    # remove ONE trailing semicolon
    if sql.endswith(";"):
        sql = sql[:-1]

    return sql.strip()
