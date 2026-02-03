---
base_model: TinyLlama/TinyLlama-1.1B-Chat-v1.0
library_name: peft
pipeline_tag: text-generation
tags:
- base_model:adapter:TinyLlama/TinyLlama-1.1B-Chat-v1.0
- lora
- transformers
---

# TRAINING-REPORT.md
## Day 2 – LoRA Adapter Setup & Parameter-Efficient Fine-Tuning

---

## Objective

The goal of Day 2 was to fine-tune a large language model using Parameter-Efficient Fine-Tuning (PEFT) techniques, specifically LoRA (Low-Rank Adaptation), while operating under limited GPU resources. The focus was on instruction-based supervised fine-tuning without modifying the full base model weights.

---

## Base Model Details

- Base Model: TinyLlama/TinyLlama-1.1B-Chat-v1.0
- Model Type: Causal Language Model
- Architecture: Decoder-only Transformer
- Language: English
- Finetuning Method: LoRA via PEFT

The TinyLlama model was selected due to its small size, chat optimization, and suitability for experimentation on free-tier GPUs.

---

## Fine-Tuning Strategy

Instead of full fine-tuning, LoRA adapters were used to reduce memory usage and computational cost.

Key characteristics:
- Base model parameters were frozen
- Only LoRA adapter weights were trainable
- Training focused on instruction-following behavior

This approach preserves the base model’s knowledge while enabling efficient task adaptation.

---

## LoRA Configuration

- Target Modules: q_proj, v_proj
- Rank (r): 8
- LoRA Alpha: 16
- LoRA Dropout: 0.05
- Bias: none
- Task Type: CAUSAL_LM

This configuration balances training stability, performance, and resource constraints.

---

## Dataset Structure

Each training sample consisted of:
- instruction
- input (optional)
- output

The dataset was split into training and validation subsets.

---

## Prompt Formatting

All samples were converted into a unified instruction-following prompt format:

### Instruction:
{instruction}

### Input:
{input}

### Response:
{output}

If the input field was empty, it was omitted from the prompt.

---

## Tokenization & Preprocessing

- Tokenizer: TinyLlama tokenizer
- Max sequence length: 512
- Truncation: Enabled
- Padding: padding="max_length"

To ensure correct loss computation during training:
- labels were explicitly set equal to input_ids
- This enabled causal language modeling loss calculation

Padding at tokenization time ensured consistent tensor shapes and prevented batch collation errors.

---

## Training Framework Decision

Initial attempts using trl’s SFTTrainer resulted in runtime failures on NVIDIA T4 GPUs due to AMP and BF16 incompatibilities, specifically errors related to gradient unscaling for BFloat16.

To maintain correctness and stability while still fulfilling Day 2 objectives:
- HuggingFace Trainer was used
- PEFT LoRA adapters were applied directly
- AMP and BF16 were disabled

This approach fully complies with Day 2 requirements, as LoRA-based PEFT was correctly implemented.

---

## Training Configuration

- Trainer: HuggingFace Trainer
- Precision: FP32
- Mixed Precision: Disabled
- Optimizer: AdamW
- Gradient Accumulation: Enabled
- Gradient Clipping: Enabled
- Evaluation Strategy: Step-based

Only LoRA parameters were updated during training.

---

## Hardware & Environment

- GPU: NVIDIA T4 (Free Tier)
- Frameworks:
  - transformers 4.33.2
  - peft 0.18.0
  - torch
  - datasets
- Operating Environment: Google Colab

---

## Verification & Validation

Training correctness was verified by:
- Confirming trainable parameters using model.print_trainable_parameters()
- Ensuring loss was computed correctly
- Running inference on custom instruction prompts
- Observing stable and coherent responses

The base model weights remained frozen throughout training.

---

## Issues Faced & Resolutions

- AMP + BF16 errors on T4 GPU: Resolved by disabling AMP and BF16
- Model not returning loss: Fixed by adding labels=input_ids
- Variable sequence length errors: Fixed using padding="max_length"
- Batch collation failures: Resolved through consistent tokenization

---

## Model Card Alignment

This training setup aligns with the generated model card metadata:
- Base model properly referenced
- PEFT and LoRA usage documented
- Fine-tuning source clearly stated
- Hardware and compute limitations acknowledged

---

## Conclusion

Day 2 objectives were successfully completed using a stable and resource-efficient LoRA-based PEFT pipeline. The implementation adheres strictly to parameter-efficient fine-tuning principles and is suitable for constrained GPU environments.

Status: Day 2 Completed Successfully  
Next Step: Day 3 – Retrieval-Augmented Generation (RAG) Integration
