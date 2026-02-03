# RETRIEVAL-STRATEGIES.md
Day 2 — Advanced Retrieval & Context Engineering

## Objective
The objective of Day 2 is to improve retrieval accuracy and reliability in a Retrieval-Augmented Generation (RAG) system by combining multiple retrieval strategies and enforcing strict context control. This directly reduces hallucinations and ensures that every generated answer is grounded in verifiable source documents.

## Limitations Observed in Day 1
Day 1 relied primarily on dense semantic vector search. While effective for capturing meaning, it introduced multiple issues such as retrieval of semantically similar but weak chunks, loss of keyword-heavy factual content, redundant context injection, and lack of strong relevance ordering.

## Retrieval Strategies Implemented

### Semantic Retrieval (Dense Search)
Semantic retrieval uses sentence embeddings generated via the `all-MiniLM-L6-v2` model and FAISS for vector similarity search. This method captures intent and conceptual similarity, making it effective for natural language queries. However, it may return contextually related but informationally thin chunks.

### Keyword Retrieval (Sparse Search – BM25)
Keyword retrieval is implemented using BM25 over tokenized chunks. This strategy excels at retrieving exact term matches, policy clauses, and structured factual information. Its limitation lies in poor performance on paraphrased or abstract queries.

### Hybrid Retrieval
Hybrid retrieval combines semantic and keyword-based results into a single candidate pool. This approach balances recall and precision by ensuring both semantic understanding and exact term relevance are preserved. The merged results form a higher-quality candidate set for further refinement.

### Deduplication
All retrieved chunks are deduplicated using their `chunk_id`. This prevents repeated or overlapping content from entering the context window and improves overall information density.

### Metadata Filtering
Optional metadata-based filters allow retrieval to be constrained by attributes such as document type, year, or source category. This ensures only valid and relevant documents participate in retrieval.

### Reranking with Cross-Encoder
A cross-encoder model (`ms-marco-MiniLM-L-6-v2`) is used to rerank retrieved chunks by jointly scoring query–chunk pairs. Unlike embeddings, the cross-encoder directly evaluates relevance, significantly improving ranking precision.

### Context Construction
Only the highest-ranked chunks are selected to build the final context. Each chunk is appended with source metadata such as file name and section ID. Context length is controlled to avoid token overflow and reduce noise.

### Source Traceability
Every context block includes explicit source references, enabling full traceability. This makes the system suitable for enterprise, compliance, and audit-driven use cases.

## End-to-End Day 2 Retrieval Flow
1. User submits a query
2. Semantic retrieval fetches top candidates
3. Keyword retrieval fetches complementary candidates
4. Results are merged into a single pool
5. Duplicate chunks are removed
6. Metadata filters are applied
7. Cross-encoder reranking refines relevance
8. Top-ranked chunks are selected
9. Final context is constructed with sources
10. Context is passed to the generation layer

## Improvements Over Day 1
Day 2 introduces hybrid retrieval, reranking, deduplication, metadata filtering, and structured context construction. These enhancements significantly improve precision, reduce hallucination risk, and make the system production-ready.

## Final Outcome
By the end of Day 2, the RAG pipeline evolves into a robust, traceable, and high-precision retrieval system. This foundation is suitable for scaling into enterprise-grade applications and advanced reasoning workflows.
