from transformers import T5Tokenizer

import torch
# Load pre-trained T5 tokenizer
tokenizer = T5Tokenizer.from_pretrained("t5-small")

# Load the cleaned PubMed dataset
import json

with open("data/processed/pubmed_cleaned.json", "r", encoding="utf-8") as f:
    pubmed_data = json.load(f)

# Tokenize the dataset
def tokenize_pubmed(example):
    inputs = tokenizer(example["document"], max_length=1024, truncation=True, padding="max_length")
    labels = tokenizer(example["summary"], max_length=150, truncation=True, padding="max_length")
    inputs["labels"] = labels["input_ids"]
    return inputs

tokenized_pubmed = [tokenize_pubmed(example) for example in pubmed_data]

print(f"✅ Tokenized PubMed dataset with {len(tokenized_pubmed)} samples!")

torch.save(tokenized_pubmed, "data/processed/tokenized_pubmed.pt")

print("Tokenized data saved successfully!")
