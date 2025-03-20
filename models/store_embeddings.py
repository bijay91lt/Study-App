import json
import os
import chromadb
import concurrent.futures
import ijson  # For streaming large JSON files
from tqdm import tqdm

# Initialize ChromaDB client and collection
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection("study_embeddings")

# Define dataset paths
dataset_folder = "datasets/embedded"
splits = ["train", "validation", "test"]

def process_entry(entry):
    """Processes a single entry and stores it in ChromaDB."""
    doc_id = entry.get("id") or str(hash(entry.get("text", "")))  # Unique identifier
    embedding = entry.get("embedding")

    if embedding:
        collection.add(ids=[doc_id], embeddings=[embedding], metadatas=[entry])
    return doc_id

def process_file(split):
    """Streams JSON file and processes it in chunks."""
    input_path = os.path.join(dataset_folder, f"{split}_embedded.json")

    with open(input_path, "r", encoding="utf-8") as f:
        data_stream = ijson.items(f, "item")  # Stream items from JSON array

        with concurrent.futures.ThreadPoolExecutor() as executor:
            list(tqdm(executor.map(process_entry, data_stream), desc=f"Processing {split}", unit="doc"))

    print(f"✅ Stored {split} embeddings in ChromaDB.")

# Process each dataset split
for split in splits:
    process_file(split)
