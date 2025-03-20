import json
import os
import time
from dotenv import load_dotenv
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

# Load Hugging Face model for embeddings
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Load environment variables
load_dotenv()
dataset_folder = "datasets/preprocessed/split"
output_folder = "datasets/embedded"
os.makedirs(output_folder, exist_ok=True)

# Function to extract text from different dataset structures
def extract_text(entry):
    return entry.get("text") or entry.get("article") or entry.get("context") or ""

def generate_embeddings(texts):
    return model.encode(texts, convert_to_tensor=True)

# Process each dataset split
splits = ["train", "validation", "test"]
for split in splits:
    input_path = os.path.join(dataset_folder, f"{split}.json")
    output_path = os.path.join(output_folder, f"{split}_embedded.json")

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    texts = [extract_text(item) for item in data]

    # Handle cases where no valid text is found
    if not texts:
        print(f"⚠️ No valid text found for {split}. Skipping.")
        continue

    print(f"🔄 Generating embeddings for {split}...")
    
    # Use tqdm to show progress
    embeddings = []
    for i in tqdm(range(0, len(texts), 32), desc=f"Processing {split}"):
        batch = texts[i:i + 32]  # Process in batches of 32 for efficiency
        batch_embeddings = generate_embeddings(batch)
        embeddings.extend(batch_embeddings)

    # Attach embeddings to dataset
    for i in range(len(data)):
        data[i]["embedding"] = embeddings[i].tolist()  # Convert tensor to list for JSON storage

    # Save embedded dataset
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"✅ Saved embeddings for {split} at {output_path}")
