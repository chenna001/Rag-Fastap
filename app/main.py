# from fastapi import FastAPI, UploadFile, File

# from app.services.pdf_service import extract_text
# from app.services.chunk_service import create_chunks


# app = FastAPI(
#     title="RAG AI Assistant",
#     description="FastAPI + RAG + LLM application",
#     version="1.0.0"
# )


# @app.get("/")
# def home():
#     return {
#         "message": "RAG AI Assistant is running"
#     }


# @app.post("/upload")
# async def upload_pdf(file: UploadFile = File(...)):

#     pdf_bytes = await file.read()

#     text = extract_text(pdf_bytes)

#     chunks = create_chunks(text)

#     return {
#         "filename": file.filename,
#         "text_length": len(text),
#         "chunk_count": len(chunks),
#         "first_chunk": chunks[0]
#     }
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ new code @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

from fastapi import FastAPI, UploadFile, File

from app.services.pdf_service import extract_text
from app.services.chunk_service import create_chunks
from app.services.embedding_service import create_embedding
from app.services.vector_service import create_vector_index


app = FastAPI(
    title="RAG AI Assistant",
    description="FastAPI + RAG + LLM application",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "RAG AI Assistant is running"
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    # 1. Read PDF
    pdf_bytes = await file.read()

    # 2. Extract text
    text = extract_text(pdf_bytes)

    # 3. Create chunks
    chunks = create_chunks(text)

    # 4. Create embeddings
    embeddings = []

    for chunk in chunks:
        embedding = create_embedding(chunk)
        embeddings.append(embedding)

    # 5. Create FAISS index
    index = create_vector_index(embeddings)

    return {
        "filename": file.filename,
        "text_length": len(text),
        "chunk_count": len(chunks),
        "vector_count": index.ntotal,
        "vector_dimension": index.d
    }