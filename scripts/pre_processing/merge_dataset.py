import json
import os

# Define paths
preprocessed_folder = "datasets/preprocessed"
output_file = os.path.join(preprocessed_folder, "merged_dataset.json")

# Dataset file paths
datasets = {
    "pdfs": os.path.join(preprocessed_folder, "pdfs.json"),
    "raw_texts": os.path.join(preprocessed_folder, "raw_texts.json"),
}

# Add summarization and flashcards_qa directories separately
structured_datasets = {
    "summarization": os.path.join(preprocessed_folder, "summarization"),
    "flashcards_qa": os.path.join(preprocessed_folder, "flashcards_qa"),
}

# Load and merge datasets
merged_data = []

# Process JSON files directly
for source, path in datasets.items():
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Add dataset source
        for item in data:
            item["source"] = source
            merged_data.append(item)
        
        print(f"✅ Merged {source} dataset ({len(data)} entries)")
    
    except Exception as e:
        print(f"❌ Error processing {source}: {e}")

# Process structured datasets (summarization & flashcards_qa)
for source, dir_path in structured_datasets.items():
    try:
        for split in ["train.json", "validation.json", "test.json"]:
            split_path = os.path.join(dir_path, split)

            if os.path.exists(split_path):
                with open(split_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                # Add dataset source and split type
                for item in data:
                    item["source"] = source
                    item["split"] = split.replace(".json", "")  # Mark train/val/test
                    merged_data.append(item)
                
                print(f"✅ Merged {source} {split} dataset ({len(data)} entries)")

    except Exception as e:
        print(f"❌ Error processing {source}: {e}")

# Save merged dataset
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(merged_data, f, ensure_ascii=False, indent=4)

print(f"✅ Merged dataset saved to {output_file}")
