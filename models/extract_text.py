import fitz  # PyMuPDF
import os
import json

# Function to extract text from a single PDF
def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    
    for page_num in range(document.page_count):
        page = document.load_page(page_num)  # Get the page
        text += page.get_text()  # Extract text from the page
    
    return text

# Process and store extracted text from PDFs
def process_pdfs(pdf_folder, output_json_path):
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    
    extracted_data = []
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_file)
        extracted_text = extract_text_from_pdf(pdf_path)
        
        if extracted_text.strip():  # Ensure the text is not empty
            extracted_data.append({
                "filename": pdf_file,
                "text": extracted_text
            })
        else:
            print(f"⚠️ No text extracted from {pdf_file}. Skipping.")

    # Save the extracted data as a JSON file
    with open(output_json_path, "w", encoding="utf-8") as json_file:
        json.dump(extracted_data, json_file, ensure_ascii=False, indent=4)
    print(f"✅ Saved extracted text from PDFs to {output_json_path}")

# Example usage
pdf_folder = "path/to/your/pdfs"  # Replace with the actual path
output_json_path = "datasets/extracted_texts_from_pdfs.json"
process_pdfs(pdf_folder, output_json_path)
