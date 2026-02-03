from typing import List, Dict
import math


def estimate_tokens(text: str) -> int:
    return math.ceil(len(text) / 4)


def deduplicate_chunks(chunks: List[Dict]) -> List[Dict]:
    seen_texts = set()
    unique_chunks = []

    for chunk in chunks:
        text = chunk.get("text", "").strip()
        if not text:
            continue
        if text in seen_texts:
            continue

        seen_texts.add(text)
        unique_chunks.append(chunk)

    return unique_chunks


def build_context(
    ranked_chunks: List[Dict],
    max_tokens: int = 3000
) -> Dict:
    final_chunks = []
    total_tokens = 0

    cleaned_chunks = deduplicate_chunks(ranked_chunks)

    for chunk in cleaned_chunks:
        chunk_text = chunk["text"]
        token_count = estimate_tokens(chunk_text)

        if total_tokens + token_count > max_tokens:
            break

        final_chunks.append({
            "chunk_id": chunk.get("chunk_id"),
            "source_file": chunk.get("source_file"),
            "section_id": chunk.get("section_id"),
            "text": chunk_text,
            "token_estimate": token_count
        })

        total_tokens += token_count

    context_text = "\n\n".join(
        f"[Source: {c['source_file']} | Section: {c['section_id']}]\n{c['text']}"
        for c in final_chunks
    )

    return {
        "context": context_text,
        "sources": [
            {
                "chunk_id": c["chunk_id"],
                "source_file": c["source_file"],
                "section_id": c["section_id"]
            }
            for c in final_chunks
        ],
        "total_tokens": total_tokens
    }
