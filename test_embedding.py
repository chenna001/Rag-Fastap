# from app.services.embedding_service import create_embedding


# text = "Australia Almond Choco"

# embedding = create_embedding(text)

# print("Embedding length:", len(embedding))
# print("First 5 values:", embedding[:5])

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from app.services.embedding_service import create_embedding


text = "Australia Almond Choco"

embedding = create_embedding(text)

print("Embedding length:", len(embedding))
print("First 5 values:", embedding[:5])