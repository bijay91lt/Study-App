from models.query_handler import answer_question
# Assuming you have extracted sections of text for question generation
def generate_flashcards(context):
    flashcards = []
    questions = ["What is the main topic?", "What are the key points?", "What is the conclusion?"]  # Example questions
    for question in questions:
        answer = answer_question(context, question)
        flashcards.append({"question": question, "answer": answer})
    return flashcards

# Example usage
flashcards = generate_flashcards("Your extracted text here from the PDF.")
for flashcard in flashcards:
    print(f"Question: {flashcard['question']}")
    print(f"Answer: {flashcard['answer']}")
