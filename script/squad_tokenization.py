import torch
import json
from transformers import AutoTokenizer

# Load a fast tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased", use_fast=True)


# Load the cleaned SQuAD 2.0 dataset
with open("data/processed/squad_cleaned.json", "r", encoding="utf-8") as f:
    squad_data = json.load(f)

# Tokenize the dataset
def tokenize_squad(example):
    question = example["question"]
    context = example["context"]
    
    encoding = tokenizer(
        question,
        context,
        truncation=True,
        padding="max_length",
        max_length=512,
        return_overflowing_tokens=True,  # ✅ Returns overflow tokens
        stride=128,  # ✅ Allows overlapping parts to be retained
        return_offsets_mapping=True,  # ✅ Helps in aligning answers
    )

    # Extract the first overflow token sequence (ignore extra ones)
    input_ids = encoding["input_ids"][0]
    attention_mask = encoding["attention_mask"][0]

    return {"input_ids": input_ids, "attention_mask": attention_mask}


tokenized_squad = [tokenize_squad(example) for example in squad_data]

print(f"✅ Tokenized SQuAD 2.0 dataset with {len(tokenized_squad)} samples!")

torch.save(tokenized_squad, "data/processed/tokenized_squad.pt")


print("Tokenized data saved successfully!")
