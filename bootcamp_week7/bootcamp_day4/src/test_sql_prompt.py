from src.pipelines.sql_pipeline import SQLPipeline

DB_CONFIG = {
    "host": "localhost",
    "dbname": "people_db",
    "user": "ravipratapsingh",
    "password": "hestabit@123",
    "port": 5432
}

pipeline = SQLPipeline(DB_CONFIG)

question = "List all people whose job title is Architect"

print(pipeline.run(question))
