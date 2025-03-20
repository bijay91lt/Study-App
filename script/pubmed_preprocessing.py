import json
import os
from datasets import load_dataset

# Load the raw PubMed dataset
pubmed_data = load_dataset("scitldr", "FullText")["train"]

cleaned_pubmed = []
for sample in pubmed_data:
    cleaned_pubmed.append({
        "document": sample["source"],  # Full research paper text
        "summary": sample["target"],   # Summarized key points
    })

# Save cleaned data
with open("data/processed/pubmed_cleaned.json", "w", encoding="utf-8") as f:
    json.dump(cleaned_pubmed, f, indent=4)

print("✅ PubMed data cleaned and saved!")
