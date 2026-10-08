from fastapi import FastAPI, UploadFile, File

from app.services.pdf_service import extract_text
from app.services.chunk_service import create_chunks


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

    pdf_bytes = await file.read()

    text = extract_text(pdf_bytes)

    chunks = create_chunks(text)

    return {
        "filename": file.filename,
        "text_length": len(text),
        "chunk_count": len(chunks),
        "first_chunk": chunks[0]
    }