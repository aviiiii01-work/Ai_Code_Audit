import json
from transformers import AutoTokenizer
import matplotlib.pyplot as plt

tokenizer = AutoTokenizer.from_pretrained(
    "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

lengths = []
clean_data = []

INPUT_FILE = "src/data/train.jsonl"
OUTPUT_FILE = "src/data/train_clean.jsonl"

with open(INPUT_FILE) as f:
    for line in f:
        item = json.loads(line)
        text = item["instruction"] + item["input"] + item["output"]
        token_len = len(tokenizer.encode(text))

        lengths.append(token_len)

        if 10 <= token_len <= 512:
            clean_data.append(item)

plt.hist(lengths, bins=40)
plt.xlabel("Token Length")
plt.ylabel("Count")
plt.title("Token Length Distribution")
plt.show()

print("Original samples:", len(lengths))
print("After cleaning:", len(clean_data))

with open(OUTPUT_FILE, "w") as f:
    for item in clean_data:
        f.write(json.dumps(item) + "\n")
