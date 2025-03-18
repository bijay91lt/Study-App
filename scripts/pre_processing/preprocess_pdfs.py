import os
import json
import re
import PyPDF2
import threading

input_folder = "datasets/pdfs/"
output_file = "datasets/preprocessed/pdfs.json"

os.makedirs("datasets/preprocessed", exist_ok=True)

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + " "
        return text.strip()
    except Exception as e:
        print(f"❌ Error processing {pdf_path}: {e}")
        return ""

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces
    text = re.sub(r"[^\w\s]", "", text)  # Remove special characters
    return text

def process_pdf(file, input_folder, data):
    pdf_path = os.path.join(input_folder, file)
    print(f"⏳ Processing {file}...")
    raw_text = extract_text_from_pdf(pdf_path)
    clean_text_data = clean_text(raw_text)
    data.append({"filename": file, "clean_text": clean_text_data})
    print(f"✅ Finished processing {file}")

data = []
threads = []

for file in os.listdir(input_folder):
    if file.endswith(".pdf"):
        thread = threading.Thread(target=process_pdf, args=(file, input_folder, data))
        threads.append(thread)
        thread.start()

for thread in threads:
    thread.join()

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"✅ Preprocessed PDFs saved to {output_file}")