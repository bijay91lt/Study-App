import json
from collections import Counter

# Load merged dataset
merged_dataset_path = "datasets/preprocessed/merged_dataset.json"

with open(merged_dataset_path, "r", encoding="utf-8") as f:
    data = json.load(f)


# Remove entries with empty text fields
filtered_data = [item for item in data if len(item.get("text", item.get("article", item.get("context", "")))) > 0]

# Remove extremely long texts (limit to 50,000 characters)
filtered_data = [item for item in filtered_data if len(item.get("text", item.get("article", item.get("context", "")))) <= 50000]

# Save cleaned dataset
cleaned_dataset_path = "datasets/preprocessed/cleaned_merged_dataset.json"
with open(cleaned_dataset_path, "w", encoding="utf-8") as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=4)

print(f"✅ Cleaning complete! Total cleaned entries: {len(filtered_data)}")