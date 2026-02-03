import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "dbname": "people_db",
    "user": "ravipratapsingh",
    "password": "hestabit@123",
    "host": "localhost",
    "port": "5432"
}

async def run_postgresql_query(query: str) -> str:
    """
    Executes a SQL query against the 'people' table. 
    Use this FIRST to retrieve data before saving it.
    """
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query)
            if cur.description:
                results = cur.fetchall()
                for row in results:
                    for k, v in row.items():
                        if hasattr(v, 'isoformat'): row[k] = v.isoformat()
                return str(results)
            conn.commit()
            return "Success."
    except Exception as e:
        return f"DB Error: {e}"
    finally:
        if 'conn' in locals(): conn.close()