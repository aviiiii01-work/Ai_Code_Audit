# Dataset Analysis — Day 1

## Domain
Coding and LLM Fundamentals

The dataset focuses on programming concepts and large language model fundamentals, including instruction following, conceptual understanding, reasoning, and structured information extraction.

---

## Dataset Source
An existing open-source instruction dataset (Alpaca-style) was used as the base data source.  
The raw dataset was processed using a custom preparation pipeline to make it suitable for low-resource fine-tuning.

---

## Dataset Preparation Pipeline
The following steps were applied using `prepare_dataset.py` and `data_cleaner.py`:

1. Loaded the open-source instruction dataset
2. Filtered samples based on token length
3. Removed extremely short and overly long examples
4. Converted data into instruction–input–output JSONL format
5. Split data into training and validation sets

---

## Dataset Size
- Training samples: ~1000
- Validation samples: ~100

This size was intentionally chosen to enable fast experimentation and stable fine-tuning in Colab environments.

---

## Task Types Covered
The dataset includes a balanced mix of instruction types:

- **QA**: Concept-based factual questions  
- **Reasoning**: Explanation and decision-based responses  
- **Extraction**: Structured information extraction from text  

This ensures the model learns both direct answering and instruction-following behavior.

---

## Token Length Analysis
- Tokenizer used: TinyLlama tokenizer
- Minimum token length: 10
- Maximum token length: 512

Token length distribution was analyzed, and outliers were removed to:
- Reduce memory usage
- Improve training stability
- Maintain consistent batch sizes during fine-tuning

---

## Conclusion
The final dataset is clean, curated, and instruction-aligned.  
It is well-suited for LoRA and QLoRA fine-tuning on low-resource hardware and follows industry-standard data preparation practices for LLM fine-tuning.
