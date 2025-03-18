from datasets import Dataset, concatenate_datasets
import json
import os

# Define dataset paths
dataset_path = "datasets/summarization"

# Read Arrow files manually
splits = ["train"]

for split in splits:
    arrow_path = f"{dataset_path}/{split}/"
    
    try:
        # Get all .arrow files in the split folder
        arrow_files = [f for f in os.listdir(arrow_path) if f.endswith(".arrow")]

        # Load all .arrow files into datasets
        datasets_list = [Dataset.from_file(os.path.join(arrow_path, f)) for f in arrow_files]

        # Concatenate if there are multiple files
        combined_dataset = concatenate_datasets(datasets_list) if len(datasets_list) > 1 else datasets_list[0]

        # Convert to list of dictionaries
        data = combined_dataset.to_pandas().to_dict(orient="records")

        # Save as JSON
        json_path = f"{dataset_path}/{split}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"✅ Converted {split} dataset to JSON: {json_path}")

    except Exception as e:
        print(f"❌ Error processing {split}: {e}")
