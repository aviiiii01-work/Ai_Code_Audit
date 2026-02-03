from datasets import load_dataset
import json
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)
    
dataset = load_dataset("tatsu-lab/alpaca", split="train")

clean_data = []

for sample in dataset:
    text = sample["instruction"] + sample["input"] + sample["output"]
    token_len = len(tokenizer.encode(text))

    if 10 <= token_len <= 512:
        clean_data.append({
            "instruction": sample["instruction"],
            "input": sample["input"],
            "output": sample["output"]
        })

clean_data = clean_data[:1100]

train_data = clean_data[:1000]
val_data = clean_data[1000:]

with open("src/data/train.jsonl", "w") as f:
    for item in train_data:
        f.write(json.dumps(item) + "\n")

with open("src/data/val.jsonl", "w") as f:
    for item in val_data:
        f.write(json.dumps(item) + "\n")

print("Train:", len(train_data))
print("Validation:", len(val_data))
