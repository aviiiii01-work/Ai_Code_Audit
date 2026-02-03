# SQL-QA-DOC.md  
Week 7 – Day 4 | Mistral + PostgreSQL (SQL Q&A Integration)

---

## 1. Objective
The objective of Day 4 is to integrate PostgreSQL with an LLM (Mistral via Ollama) so that natural language questions can be converted into SQL queries, executed on a relational database, and the results returned in a human-readable form.

This setup is intentionally non-production and is designed for learning, experimentation, and understanding how LLMs interact with structured SQL data.

---

## 2. Tech Stack
- Database: PostgreSQL (local)
- LLM: Mistral (via Ollama)
- Backend Language: Python
- Database Connector: psycopg2
- Environment: Local development using virtual environment (venv)

---

## 3. Database Setup Summary
- Database Name: people_db
- Table Name: people

Table Schema:
- id (SERIAL, PRIMARY KEY)
- user_id (TEXT)
- first_name (TEXT)
- last_name (TEXT)
- sex (TEXT)
- email (TEXT)
- phone (TEXT)
- date_of_birth (DATE)
- job_title (TEXT)

Ownership and permissions were fixed by:
- Changing table owner to the local user
- Changing sequence owner to the local user
- Changing public schema owner to the local user
- Ensuring full privileges on tables and sequences

---

## 4. CSV Import Issue and Resolution

### Problem
While importing data using \\copy, multiple errors were encountered:
- extra data after last expected column
- column "dummy" of relation "people" does not exist

### Root Cause
The CSV file contained one extra column at the beginning that did not exist in the people table. PostgreSQL \\copy requires an exact match between CSV columns and table columns.

### Solution
The extra column was removed from the CSV file before importing.

CSV cleaning was done by skipping the first column and creating a cleaned file. The cleaned CSV was then successfully imported into the people table.

---

## 5. SQL Q&A High-Level Flow
1. User asks a question in natural language.
2. The question is passed to Mistral.
3. Mistral converts the question into a SQL query using schema context.
4. The generated SQL query is executed on PostgreSQL.
5. Query results are fetched.
6. Mistral formats or summarizes the results into a natural language response.

---

## 6. Example: Natural Language to SQL

User Question:
Show all people who are Probation officers.

Generated SQL Logic:
Select first name, last name, and job title from the people table where job title is Probation officer.

---

## 7. Python Integration (Conceptual)
- Establish a PostgreSQL connection using psycopg2
- Provide table schema context to Mistral
- Convert user input into SQL
- Execute SQL query safely
- Fetch results
- Pass results back to Mistral for summarization

This demonstrates how an LLM can act as an intelligent SQL reasoning layer on top of structured data.

---

## 8. Key Learnings
- PostgreSQL \\copy is strict about column order and count
- CSV preprocessing is often required before ingestion
- Ownership and permissions are critical even in local setups
- LLMs can generate accurate SQL when schema context is provided
- This architecture is the base for text-to-SQL and SQL-based RAG systems

---

## 9. Current Status
- PostgreSQL installed and configured
- people_db database ready
- CSV data successfully ingested into people table
- Environment ready for Mistral-based SQL Q&A

---

## 10. Next Steps
- Add schema-aware prompting for Mistral
- Restrict generated queries to SELECT-only
- Wrap SQL execution in a clean Python service layer
- Add logging and query tracking
- Extend towards a structured-data RAG pipeline

---

End of Week 7 Day 4 – SQL Q&A Documentation
