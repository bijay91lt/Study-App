from datasets import load_dataset
import json

# Load PubMed dataset
pubmed_dataset = load_dataset("scitldr", "FullText", trust_remote_code=True)

# Load SQuAD 2.0 dataset
squad_dataset = load_dataset("squad_v2")

# Save datasets locally
pubmed_dataset.save_to_disk("data/raw/pubmed")
squad_dataset.save_to_disk("data/raw/squad")

print("✅ Datasets downloaded and saved!")
