import os
import json
import argparse
from models.extract_text import extract_text_from_pdf
from models.generate_embeddings import generate_embeddings
from models.store_embeddings import store_in_chroma
from models.query_handler import query_model
from models.summarizer import summarize_text
from models.flashcard_generator import generate_flashcards

# Set up argument parsing
parser = argparse.ArgumentParser(description="Personalized Study Assistant")
parser.add_argument("--pdf", type=str, help="Path to the PDF file")
parser.add_argument("--query", type=str, help="Ask a question from the document")
parser.add_argument("--summarize", action="store_true", help="Summarize the document")
parser.add_argument("--flashcards", action="store_true", help="Generate flashcards")
args = parser.parse_args()

if args.pdf:
    print("\n📄 Extracting text from PDF...")
    extracted_text = extract_text_from_pdf(args.pdf)
    print("✅ Text extracted successfully.")

    # Save extracted text temporarily
    temp_text_file = "temp_extracted_text.json"
    with open(temp_text_file, "w", encoding="utf-8") as f:
        json.dump({"text": extracted_text}, f)

    print("\n🧠 Generating embeddings...")
    embeddings = generate_embeddings(extracted_text)
    print("✅ Embeddings generated.")

    print("\n💾 Storing embeddings in ChromaDB...")
    store_in_chroma(extracted_text, embeddings)
    print("✅ Embeddings stored successfully.")

if args.query:
    print("\n🔍 Searching for relevant information...")
    answer = query_model(args.query)
    print(f"🤖 Answer: {answer}")

if args.summarize:
    print("\n📚 Generating summary...")
    summary = summarize_text(extracted_text)
    print(f"📌 Summary:\n{summary}")

if args.flashcards:
    print("\n🃏 Generating flashcards...")
    flashcards = generate_flashcards(extracted_text)
    print("\nFlashcards:")
    for i, card in enumerate(flashcards, 1):
        print(f"{i}. Q: {card['question']} \n   A: {card['answer']}\n")
