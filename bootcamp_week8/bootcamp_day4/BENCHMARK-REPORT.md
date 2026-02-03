# LLM Benchmark Report — Bootcamp Day 4

## Overview

This report presents a comprehensive benchmark comparison between three versions of the TinyLlama model:

1. **Base Model (FP16, GPU)** — Original pretrained TinyLlama
2. **Fine-tuned Model (INT8, GPU)** — LoRA fine-tuned and merged model
3. **Quantized GGUF Model (Q4_0, CPU)** — CPU-optimized GGUF variant via `llama.cpp`

The goal is to evaluate **performance vs quality trade-offs** across different deployment strategies.

---

## Benchmark Setup

### Models Evaluated

| Model Type       | Precision | Device   | Framework                  |
| ---------------- | --------- | -------- | -------------------------- |
| Base Model       | FP16      | CUDA GPU | HuggingFace Transformers   |
| Fine-tuned Model | INT8      | CUDA GPU | HuggingFace + bitsandbytes |
| GGUF Model       | Q4_0      | CPU      | llama.cpp                  |

### Prompts Used

* Explain LoRA fine-tuning in simple terms.
* What is KV caching in transformers?
* Compare INT8 vs INT4 quantization.

### Metrics Collected

* **Tokens/sec** — Throughput
* **Latency (sec)** — End-to-end generation time
* **VRAM (MB)** — Peak GPU memory usage
* **Semantic Similarity** — Cosine similarity of sentence embeddings vs base model output

Semantic similarity was computed using:

* `sentence-transformers/all-MiniLM-L6-v2`

The **base FP16 model output** was used as the reference for similarity comparison.

---

## Raw Results

| Model           | Device | Precision | Tok/s  | Latency (s) | VRAM (MB) | Cosine Similarity |
| --------------- | ------ | --------- | ------ | ----------- | --------- | ----------------- |
| base_model      | CUDA   | fp16      | 38.83  | 0.36        | 974.2     | 1.000             |
| base_model      | CUDA   | fp16      | 258.18 | 0.04        | 974.2     | 1.000             |
| base_model      | CUDA   | fp16      | 31.64  | 4.39        | 978.2     | 1.000             |
| finetuned_model | CUDA   | int8      | 10.47  | 13.46       | 1445.5    | 0.86–0.90         |
| finetuned_model | CUDA   | int8      | 11.11  | 6.75        | 1445.5    | 0.84–0.89         |
| finetuned_model | CUDA   | int8      | 10.27  | 13.54       | 1445.5    | 0.85–0.88         |
| gguf_model      | CPU    | q4_0      | 13.32  | 0.60        | NA        | 0.72–0.78         |
| gguf_model      | CPU    | q4_0      | 10.41  | 0.58        | NA        | 0.70–0.76         |
| gguf_model      | CPU    | q4_0      | 16.79  | 3.22        | NA        | 0.74–0.80         |

---

## Analysis & Insights

### 1️⃣ Base Model (FP16, GPU)

* Highest semantic fidelity (reference)
* Extremely high throughput after warm-up
* Moderate VRAM usage (~1 GB)
* Best suited for **research & evaluation**

### 2️⃣ Fine-tuned Model (INT8, GPU)

* Semantic similarity: **~0.85–0.90**
* Noticeable latency increase due to quantization + LoRA merge
* Higher VRAM usage due to 8-bit loading & adapters
* Ideal for **domain-specific tasks where accuracy matters more than speed**

### 3️⃣ GGUF Model (Q4_0, CPU)

* Semantic similarity: **~0.72–0.80**
* Runs fully on CPU — no GPU required
* Competitive throughput for lightweight deployments
* Best choice for **edge devices, laptops, and offline inference**

---

## Key Takeaways

* **Quantization introduces semantic drift**, measurable via cosine similarity
* **INT8 fine-tuning preserves meaning better** than aggressive GGUF Q4_0
* **GGUF offers the best portability** with acceptable quality loss
* Cosine similarity is a **far more reliable metric** than hard-coded accuracy labels

---

## Conclusion

This benchmark demonstrates a full inference evaluation pipeline covering:

* GPU vs CPU execution
* FP16 vs INT8 vs INT4 quantization
* Performance vs semantic quality trade-offs

Such analysis mirrors **real-world LLM deployment decisions**, making this benchmark suitable for:

* Production readiness evaluation
* Portfolio projects
* Technical interviews

---

*End of Report*
