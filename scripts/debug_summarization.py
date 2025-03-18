import os

input_folder = "datasets/flashcards_qa/"

for file in os.listdir(input_folder):
    if file.endswith(".txt"):
        with open(os.path.join(input_folder, file), "r", encoding="utf-8") as f:
            lines = f.readlines()
        print(f"📄 File: {file}\n🔹 First 5 Lines:\n{lines[:5]}\n")
        break
