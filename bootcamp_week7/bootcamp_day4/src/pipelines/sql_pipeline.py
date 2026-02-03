from src.utils.schema_loader import SchemaLoader
from src.generator.sql_generator import SQLPromptGenerator
from src.llm.ollama_client import OllamaClient
from src.utils.sql_validator import validate_sql
from src.utils.sql_executor import execute_sql
from src.utils.result_summarizer import summarize_result

class SQLPipeline:
    def __init__(self, conn_params: dict):
        self.schema_loader = SchemaLoader(conn_params)
        self.llm = OllamaClient()
        self.conn_params = conn_params

    def run(self, question: str):
        schema_text = self.schema_loader.get_schema_text()

        prompt = SQLPromptGenerator(schema_text).build_prompt(question)

        sql_query = self.llm.generate(prompt).strip()
        print("\nRAW LLM OUTPUT:\n", sql_query)

        if sql_query.endswith(";"):
            sql_query = sql_query[:-1]

        validate_sql(sql_query)

        rows, columns = execute_sql(sql_query, self.conn_params)

        return summarize_result(question, rows, columns)
