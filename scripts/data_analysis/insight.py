import json
from collections import Counter

# Load merged dataset
merged_dataset_path = "datasets/preprocessed/cleaned_merged_dataset.json"

with open(merged_dataset_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Check total dataset size
print(f"Total entries: {len(data)}\n")

# Count entries per source
source_counts = Counter(item["source"] for item in data)
print("Dataset distribution by source:")
for source, count in source_counts.items():
    print(f"  {source}: {count}")

# Check for missing text fields
missing_texts = sum(1 for item in data if "text" not in item and "article" not in item and "context" not in item)
print(f"\nMissing text fields: {missing_texts}")

# Check length distribution
text_lengths = [len(item.get("text", item.get("article", item.get("context", "")))) for item in data]
print(f"Average text length: {sum(text_lengths) / len(text_lengths):.2f} characters")
print(f"Max text length: {max(text_lengths)} characters")
print(f"Min text length: {min(text_lengths)} characters")
