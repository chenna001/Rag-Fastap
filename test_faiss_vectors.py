from app.services.embedding_service import create_embedding
from app.services.vector_service import create_vector_index


texts = [
    "Australia Almond Choco",
    "Australia sales report",
    "Product sales amount"
]


embeddings = []

for text in texts:
    embedding = create_embedding(text)
    embeddings.append(embedding)


index = create_vector_index(embeddings)


print("FAISS index created")
print("Dimension:", index.d)
print("Number of vectors:", index.ntotal)