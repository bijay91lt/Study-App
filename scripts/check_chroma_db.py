import chromadb

# Load ChromaDB client
chroma_client = chromadb.PersistentClient(path="chroma_db")

# Get collection
collection = chroma_client.get_collection("study_embeddings")

# Fetch all stored documents
stored_data = collection.get(include=["documents"])

# Print stored documents
print("\n🔍 Stored Documents in ChromaDB:")
print(stored_data.get("documents", []))
