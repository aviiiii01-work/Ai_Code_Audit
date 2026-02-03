import psycopg2

class SchemaLoader:
    def __init__(self, conn_params: dict):
        self.conn = psycopg2.connect(
            host=conn_params["host"],
            dbname=conn_params["dbname"],
            user=conn_params["user"],
            password=conn_params["password"],
            port=conn_params.get("port", 5432)
        )

    def load_schema(self):
        query = """
        SELECT
            table_name,
            column_name,
            data_type
        FROM information_schema.columns
        WHERE table_schema = 'public'
        ORDER BY table_name, ordinal_position;
        """

        cur = self.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()

        schema = {}
        for table, column, dtype in rows:
            schema.setdefault(table, []).append((column, dtype))

        return schema

    def get_schema_text(self):
        schema = self.load_schema()
        return self.to_text(schema)

    def to_text(self, schema):
        lines = []
        for table, columns in schema.items():
            lines.append(f"Table: {table}")
            for col, dtype in columns:
                lines.append(f"  - {col}: {dtype}")
            lines.append("")
        return "\n".join(lines)

    def close(self):
        self.conn.close()
