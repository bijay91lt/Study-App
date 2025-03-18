import os
import json

input_folder = "datasets/flashcards_qa/"
output_file = "datasets/preprocessed/flashcards_qa.json"

data = []

for file in os.listdir(input_folder):
    if file.endswith(".txt"):
        with open(os.path.join(input_folder, file), "r", encoding="utf-8") as f:
            lines = f.readlines()

        qa_pairs = [{"question": lines[i].strip(), "answer": lines[i+1].strip()} for i in range(0, len(lines), 2)]
        data.extend(qa_pairs)

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"✅ Flashcards & Q&A dataset saved to {output_file}")
