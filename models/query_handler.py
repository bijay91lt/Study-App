from transformers import pipeline

# Load pre-trained DistilBERT model for question answering
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Function to get answer for a question
def answer_question(context, question):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

# Example usage
context = "Your extracted text here from the PDF."
question = "What is the main topic?"
answer = answer_question(context, question)
print(f"Answer: {answer}")
