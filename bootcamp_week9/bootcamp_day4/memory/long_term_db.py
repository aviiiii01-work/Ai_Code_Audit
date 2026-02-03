import aiosqlite
import os

DB_PATH = "data/long_term.db"

async def init_db():
    os.makedirs("data", exist_ok=True)
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("CREATE TABLE IF NOT EXISTS facts (id INTEGER PRIMARY KEY, fact TEXT)")
        await db.commit()

async def save_to_long_term_db(fact: str) -> str:
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("INSERT INTO facts (fact) VALUES (?)", (fact,))
        await db.commit()
    return f"Successfully saved to DB: {fact}"

async def get_all_db_facts() -> str:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT fact FROM facts") as cursor:
            rows = await cursor.fetchall()
            if not rows: return "The database is currently empty."
            return "Permanent Records: " + ", ".join([row[0] for row in rows])