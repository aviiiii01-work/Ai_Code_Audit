import psycopg2

def execute_sql(sql: str, conn_params: dict):
    conn = psycopg2.connect(
        host=conn_params["host"],
        dbname=conn_params["dbname"],
        user=conn_params["user"],
        password=conn_params["password"],
        port=conn_params.get("port", 5432)
    )

    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]

    cur.close()
    conn.close()

    return rows, columns
