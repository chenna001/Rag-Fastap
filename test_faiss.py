from app.services.vector_service import create_vector_index


index = create_vector_index()

print("FAISS index created")
print("Dimension:", index.d)
print("Number of vectors:", index.ntotal)