import os
import json
import uuid
from pathlib import Path

import pandas as pd
from PyPDF2 import PdfReader
from docx import Document
import yaml

settings_path = Path(__file__).resolve().parents[1] / "config" / "settings.yaml"

with open(settings_path, "r") as f:
    config = yaml.safe_load(f)

RAW_DATA_DIR = config["data_paths"]["raw"]
CHUNKS_DIR = config["data_paths"]["chunks"]
CHUNK_SIZE = config["chunking"]["chunk_size"]
CHUNK_OVERLAP = config["chunking"]["chunk_overlap"]


def load_text_file(file_path):  
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception:
        return ""


def load_pdf_file(file_path):
    reader = PdfReader(file_path)
    extracted_pages = []
    for page_index, page in enumerate(reader.pages):
        page_text = page.extract_text()
        if page_text:
            extracted_pages.append((page_index + 1, page_text))
    return extracted_pages


def load_docx_file(file_path):
    doc = Document(file_path)
    sections = []
    for idx, para in enumerate(doc.paragraphs):
        if para.text.strip():
            sections.append((idx + 1, para.text))
    return sections


def load_csv_file(file_path):
    df = pd.read_csv(file_path)
    rows = []
    for idx, row in df.iterrows():
        row_text = " | ".join([str(val) for val in row.values])
        rows.append((idx + 1, row_text))
    return rows


def basic_text_cleaning(text):
    if not text:
        return ""
    text = text.replace("\n", " ")
    text = " ".join(text.split())
    return text.strip()


def split_text_into_chunks(text, chunk_size, overlap):
    chunks = []
    start_index = 0
    text_length = len(text)
    while start_index < text_length:
        end_index = start_index + chunk_size
        chunk = text[start_index:end_index]
        if chunk.strip():
            chunks.append(chunk)
        start_index = end_index - overlap
        if start_index < 0:
            start_index = 0
    return chunks


def extract_chunks_from_file(file_path):
    file_extension = file_path.suffix.lower()
    collected_chunks = []

    if file_extension == ".txt":
        raw_text = load_text_file(file_path)
        cleaned_text = basic_text_cleaning(raw_text)
        sections = [(None, cleaned_text)]

    elif file_extension == ".pdf":
        sections = load_pdf_file(file_path)
        sections = [(page, basic_text_cleaning(text)) for page, text in sections]

    elif file_extension == ".docx":
        sections = load_docx_file(file_path)
        sections = [(sec, basic_text_cleaning(text)) for sec, text in sections]

    elif file_extension == ".csv":
        sections = load_csv_file(file_path)
        sections = [(row, basic_text_cleaning(text)) for row, text in sections]

    else:
        return []

    for section_id, section_text in sections:
        if not section_text:
            continue
        text_chunks = split_text_into_chunks(section_text, CHUNK_SIZE, CHUNK_OVERLAP)
        for chunk_text in text_chunks:
            chunk_data = {
                "chunk_id": str(uuid.uuid4()),
                "source_file": file_path.name,
                "section_id": section_id,
                "text": chunk_text,
                "char_count": len(chunk_text),
                "token_estimate": len(chunk_text) // 4
            }
            collected_chunks.append(chunk_data)

    return collected_chunks


def ingest_files_from_raw_folder():
    raw_data_path = Path(RAW_DATA_DIR)
    output_path = Path(CHUNKS_DIR)
    output_path.mkdir(parents=True, exist_ok=True)
    output_file = output_path / "chunks.jsonl"

    with open(output_file, "w", encoding="utf-8") as writer:
        for file in raw_data_path.iterdir():
            if not file.is_file():
                continue
            file_chunks = extract_chunks_from_file(file)
            for chunk in file_chunks:
                writer.write(json.dumps(chunk) + "\n")

    print(f"Finished ingestion. Chunks stored at: {output_file}")


if __name__ == "__main__":
    ingest_files_from_raw_folder()
