import time
import torch
import csv
import os
from transformers import AutoTokenizer, AutoModelForCausalLM
from llama_cpp import Llama
from sentence_transformers import SentenceTransformer, util

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))

BENCHMARK_DIR = os.path.join(PROJECT_ROOT, "benchmarks")
RESULTS_PATH = os.path.join(BENCHMARK_DIR, "results.csv")

FT_MODEL_PATH = os.path.join(PROJECT_ROOT, "merged_model")
GGUF_MODEL_PATH = os.path.join(PROJECT_ROOT, "quantized", "model.gguf")

os.makedirs(BENCHMARK_DIR, exist_ok=True)

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

PROMPTS = [
    "Explain LoRA fine-tuning in simple terms.",
    "What is KV caching in transformers?",
    "Compare INT8 vs INT4 quantization."
]

embedder = SentenceTransformer("all-MiniLM-L6-v2")

def cosine_similarity(a, b):
    emb_a = embedder.encode(a, convert_to_tensor=True)
    emb_b = embedder.encode(b, convert_to_tensor=True)
    return float(util.cos_sim(emb_a, emb_b)[0][0])

def get_vram_mb():
    if torch.cuda.is_available():
        return torch.cuda.max_memory_allocated() / 1024 ** 2
    return 0.0


def generate_hf(model, tokenizer, prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(DEVICE)
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=128, use_cache=True)
    return tokenizer.decode(output[0], skip_special_tokens=True)


def benchmark_model(model, tokenizer, model_name, precision, reference_outputs):
    if torch.cuda.is_available():
        torch.cuda.reset_peak_memory_stats()

    for i, prompt in enumerate(PROMPTS):
        start = time.time()
        text = generate_hf(model, tokenizer, prompt)
        latency = time.time() - start

        tokens = len(text.split())
        tokens_per_sec = tokens / latency if latency > 0 else 0
        vram = get_vram_mb()

        similarity = cosine_similarity(reference_outputs[i], text)

        with open(RESULTS_PATH, "a", newline="") as f:
            csv.writer(f).writerow([
                model_name,
                DEVICE,
                precision,
                round(tokens_per_sec, 2),
                round(latency, 2),
                round(vram, 1),
                round(similarity, 4)
            ])

        print(model_name, precision, f"{tokens_per_sec:.2f} tok/s", f"sim={similarity:.3f}")


def benchmark_gguf(model_path, reference_outputs):
    llm = Llama(model_path=model_path, n_ctx=2048, n_threads=os.cpu_count())

    for i, prompt in enumerate(PROMPTS):
        start = time.time()
        output = llm(prompt, max_tokens=128)
        latency = time.time() - start

        text = output["choices"][0]["text"]
        tokens = len(text.split())
        tokens_per_sec = tokens / latency if latency > 0 else 0

        similarity = cosine_similarity(reference_outputs[i], text)

        with open(RESULTS_PATH, "a", newline="") as f:
            csv.writer(f).writerow([
                "gguf_model",
                "cpu",
                "q4_0",
                round(tokens_per_sec, 2),
                round(latency, 2),
                "NA",
                round(similarity, 4)
            ])

        print("gguf_model q4_0", f"{tokens_per_sec:.2f} tok/s", f"sim={similarity:.3f}")


def main():
    with open(RESULTS_PATH, "w", newline="") as f:
        csv.writer(f).writerow([
            "model",
            "device",
            "precision",
            "tokens_per_sec",
            "latency_sec",
            "vram_mb",
            "accuracy_notes"
        ])

    base_model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

    tokenizer = AutoTokenizer.from_pretrained(base_model_id)
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_id,
        torch_dtype=torch.float16,
        device_map="auto"
    ).eval()

    reference_outputs = [
        generate_hf(base_model, tokenizer, p) for p in PROMPTS
    ]

    benchmark_model(base_model, tokenizer, "base_model", "fp16", reference_outputs)

    tokenizer = AutoTokenizer.from_pretrained(FT_MODEL_PATH)
    ft_model = AutoModelForCausalLM.from_pretrained(
        FT_MODEL_PATH,
        load_in_8bit=True,
        device_map="auto"
    ).eval()

    benchmark_model(ft_model, tokenizer, "finetuned_model", "int8", reference_outputs)

    benchmark_gguf(GGUF_MODEL_PATH, reference_outputs)


if __name__ == "__main__":
    main()
