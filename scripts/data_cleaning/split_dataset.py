import json
import random
import os

# Load the merged dataset
input_file = "datasets/preprocessed/cleaned_merged_dataset.json"
output_dir = "datasets/preprocessed/split/"
os.makedirs(output_dir, exist_ok=True)

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Shuffle data to ensure randomness
random.shuffle(data)

# Compute split sizes
total = len(data)
train_size = int(0.8 * total)
val_size = int(0.1 * total)

data_splits = {
    "train": data[:train_size],
    "validation": data[train_size:train_size + val_size],
    "test": data[train_size + val_size:]
}

# Save each split
for split_name, split_data in data_splits.items():
    output_file = os.path.join(output_dir, f"{split_name}.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(split_data, f, ensure_ascii=False, indent=4)
    print(f"✅ {split_name.capitalize()} set saved: {output_file} ({len(split_data)} entries)")
