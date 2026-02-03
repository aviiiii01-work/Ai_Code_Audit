import psycopg2

class SQLExecutor:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="people_db",
            user="ravipratapsingh",
            password="hestabit@123",
            host="localhost",
            port=5432
        )

    def run(self, sql: str):
        with self.conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
            columns = [d[0] for d in cur.description]
        return columns, rows
