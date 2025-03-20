import chromadb
import os
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

# Load environment variables (if any)
load_dotenv()

# Load Sentence Transformer model (same as used for embedding)
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Initialize ChromaDB client and load collection
chroma_client = chromadb.PersistentClient(path="chroma_db")  # Ensure correct DB path
collection = chroma_client.get_collection("study_embeddings")  # Collection name used in Step 3

def search_documents(query_text, top_k=5):
    """Retrieve the most relevant documents from ChromaDB based on query."""
    
    # Convert query to vector embedding
    query_embedding = embedding_model.encode(query_text).tolist()

    # Perform similarity search
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    # Extract retrieved documents
    documents = results.get("documents", [[]])[0]  # Extracting first result list
    scores = results.get("distances", [[]])[0]  # Extracting similarity scores

    # Print results
    print("\n🔍 **Retrieved Documents:**")
    for i, doc in enumerate(documents):
        print(f"{i+1}. Score: {scores[i]:.4f} ➝ {doc}")

    return documents

# Example Usage
if __name__ == "__main__":
    user_query = input("Enter your search query: ")
    retrieved_docs = search_documents(user_query)
