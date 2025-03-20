from datasets import load_dataset
import json
# Load raw SQuAD dataset
squad_data = load_dataset("squad_v2")["train"]

cleaned_squad = []
for sample in squad_data:
    cleaned_squad.append({
        "context": sample["context"],   # The passage
        "question": sample["question"], # The generated question
        "answer": sample["answers"]["text"],  # List of possible answers
    })

# Save cleaned data
with open("data/processed/squad_cleaned.json", "w", encoding="utf-8") as f:
    json.dump(cleaned_squad, f, indent=4)

print("✅ SQuAD 2.0 data cleaned and saved!")
