from datasets import load_dataset

dataset = load_dataset("squad")
dataset.save_to_disk("datasets/flashcards_qa/")
print("✅ Q&A dataset downloaded.")
