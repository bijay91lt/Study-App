import os
import re
import json

input_folder = "datasets/raw_texts/"
output_file = "datasets/preprocessed/raw_texts.json"

os.makedirs("datasets/preprocessed", exist_ok=True)

def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces
    text = re.sub(r"[^\w\s]", "", text)  # Remove special characters
    text = text.strip()
    return text

data = []

for file in os.listdir(input_folder):
    if file.endswith(".txt"):
        with open(os.path.join(input_folder, file), "r", encoding="utf-8") as f:
            text = f.read()

        clean_text_data = clean_text(text)
        data.append({"filename": file, "clean_text": clean_text_data})

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"✅ Preprocessed raw texts saved to {output_file}")
