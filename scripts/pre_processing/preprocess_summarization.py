import os
import re
import json

input_folder = "datasets/summarization/"
output_file = "datasets/preprocessed/summarization.json"

os.makedirs("datasets/preprocessed", exist_ok=True)

def clean_text(text):
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces
    text = re.sub(r"\[.*?\]", "", text)  # Remove references like [1], [2]
    text = text.strip()
    return text

data = []

for file in os.listdir(input_folder):
    if file.endswith(".txt"):
        with open(os.path.join(input_folder, file), "r", encoding="utf-8") as f:
            summary = f.read()

        clean_summary = clean_text(summary)
        data.append({"text": clean_summary, "summary": summary})

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"✅ Summarization dataset saved to {output_file}")
