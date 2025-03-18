import os
import re
import json
import concurrent.futures

# Define dataset paths
input_folder = "datasets/flashcards_qa/"
output_folder = "datasets/preprocessed/flashcards_qa/"
os.makedirs(output_folder, exist_ok=True)  # Ensure the summarization directory exists

# Function to clean text
def clean_text(text):
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces
    text = re.sub(r"\[.*?\]", "", text)  # Remove references like [1], [2]
    return text.strip()

# Function to process a JSON file
def process_json(file):
    file_path = os.path.join(input_folder, file)
    output_path = os.path.join(output_folder, file)
    
    try:
        # Load JSON data
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Preprocess text fields
        for item in data:
            if "text" in item:
                item["text"] = clean_text(item["text"])
            if "summary" in item:
                item["summary"] = clean_text(item["summary"])

        # Save processed JSON
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print(f"✅ Processed: {file} → {output_path}")
    
    except Exception as e:
        print(f"❌ Error processing {file}: {e}")

# List of JSON files to process
json_files = ["train.json", "validation.json"]

# Use multi-threading to process all JSON files
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(process_json, json_files)

print("\n✅ Preprocessing complete! Files saved in:", output_folder)
