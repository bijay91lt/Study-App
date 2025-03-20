from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# Load pre-trained T5 model for summarization
model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")

# Function to summarize text
def summarize(text):
    inputs = tokenizer("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(inputs["input_ids"], max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Example usage
text = "Your extracted text here from the PDF."
summary = summarize(text)
print(f"Summary: {summary}")
