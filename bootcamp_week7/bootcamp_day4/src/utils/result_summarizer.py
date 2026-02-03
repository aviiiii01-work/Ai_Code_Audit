def summarize_result(question, rows, columns):
    if not rows:
        return "No results found."

    summary = f"Question: {question}\n"
    summary += f"Total rows: {len(rows)}\n\n"

    summary += "Sample results:\n"
    for row in rows[:5]:
        summary += str(dict(zip(columns, row))) + "\n"

    return summary
