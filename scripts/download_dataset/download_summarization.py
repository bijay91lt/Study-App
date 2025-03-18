from datasets import load_dataset

dataset = load_dataset("cnn_dailymail", "3.0.0")
dataset.save_to_disk("datasets/summarization/")
print("✅ CNN/DailyMail summarization dataset downloaded.")