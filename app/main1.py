
# import traceback

# from fastapi import FastAPI, UploadFile, File, HTTPException

# from app.services.document_service import extract_document_text
# from app.services.chunk_service import create_chunks
# from app.services.embedding_service import create_embedding
# from app.services.vector_service import create_vector_index


# app = FastAPI(
#     title="Multi-Format RAG AI Assistant",
#     description="Upload PDF, Word, Excel, CSV, TXT and PowerPoint files",
#     version="1.0.0"
# )


# @app.get("/")
# def home():
#     return {
#         "message": "Multi-Format RAG AI Assistant is running"
#     }


# @app.post("/upload")
# async def upload_document(file: UploadFile = File(...)):

#     try:
#         # 1. Check filename
#         filename = file.filename or ""

#         if not filename:
#             raise HTTPException(
#                 status_code=400,
#                 detail="Filename is missing"
#             )

#         # 2. Read uploaded file
#         file_bytes = await file.read()

#         if not file_bytes:
#             raise HTTPException(
#                 status_code=400,
#                 detail="Uploaded file is empty"
#             )

#         print(f"Uploaded file: {filename}")
#         print(f"File size: {len(file_bytes)} bytes")

#         # 3. Extract text from the document
#         print("Step 1: Extracting document text...")

#         text = extract_document_text(
#             filename,
#             file_bytes
#         )

#         print(f"Extracted characters: {len(text)}")

#         if not text.strip():
#             raise HTTPException(
#                 status_code=400,
#                 detail="No extractable text found in document"
#             )

#         # 4. Split text into chunks
#         print("Step 2: Creating chunks...")

#         chunks = create_chunks(text)

#         if not chunks:
#             raise HTTPException(
#                 status_code=400,
#                 detail="No text chunks were created"
#             )

#         print(f"Number of chunks: {len(chunks)}")

#         # 5. Generate Gemini embeddings
#         print("Step 3: Generating Gemini embeddings...")

#         embeddings = []

#         for i, chunk in enumerate(chunks, start=1):
#             print(f"Embedding chunk {i}/{len(chunks)}")

#             embedding = create_embedding(chunk)
#             embeddings.append(embedding)

#         print(f"Embeddings created: {len(embeddings)}")

#         # 6. Create FAISS vector index
#         print("Step 4: Creating FAISS index...")

#         index = create_vector_index(embeddings)

#         print("Upload processing completed successfully")

#         # 7. Return response
#         return {
#             "filename": filename,
#             "text_length": len(text),
#             "chunk_count": len(chunks),
#             "vector_count": index.ntotal,
#             "vector_dimension": index.d,
#             "message": "Document processed successfully"
#         }

#     except HTTPException:
#         raise

#     except Exception as exc:
#         print("\nERROR DURING DOCUMENT UPLOAD")
#         print(traceback.format_exc())

#         raise HTTPException(
#             status_code=500,
#             detail=f"{type(exc).__name__}: {exc}"
#         ) from exc
##### new code add

import traceback

from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel

from app.services.document_service import extract_document_text
from app.services.chunk_service import create_chunks
from app.services.embedding_service import create_embedding
from app.services.vector_service import (
    add_chunks_to_index,
    search_chunks,
)
from app.services.llm_service import generate_answer


app = FastAPI(
    title="Multi-Format RAG AI Assistant",
    description="Upload documents and ask questions using RAG",
    version="1.0.0",
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Multi-Format RAG AI Assistant is running"
    }


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        filename = file.filename or ""

        if not filename:
            raise HTTPException(
                status_code=400,
                detail="Filename is missing",
            )

        file_bytes = await file.read()

        if not file_bytes:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty",
            )

        print(f"Uploaded file: {filename}")
        print(f"File size: {len(file_bytes)} bytes")

        # Step 1: Extract document text
        print("Step 1: Extracting document text...")
        text = extract_document_text(filename, file_bytes)

        print(f"Extracted characters: {len(text)}")

        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="No extractable text found in document",
            )

        # Step 2: Create chunks
        print("Step 2: Creating chunks...")
        chunks = create_chunks(text)

        if not chunks:
            raise HTTPException(
                status_code=400,
                detail="No text chunks were created",
            )

        print(f"Number of chunks: {len(chunks)}")

        # Step 3: Generate embeddings
        print("Step 3: Generating Gemini embeddings...")
        embeddings = []

        for i, chunk in enumerate(chunks, start=1):
            print(f"Embedding chunk {i}/{len(chunks)}")
            embeddings.append(create_embedding(chunk))

        print(f"Embeddings created: {len(embeddings)}")

        # Step 4: Store vectors and matching chunks
        print("Step 4: Adding vectors to FAISS...")
        add_chunks_to_index(chunks, embeddings)

        return {
            "filename": filename,
            "text_length": len(text),
            "chunk_count": len(chunks),
            "message": "Document processed successfully",
        }

    except HTTPException:
        raise

    except Exception as exc:
        print("\nERROR DURING DOCUMENT UPLOAD")
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=f"{type(exc).__name__}: {exc}",
        ) from exc

    finally:
        await file.close()


@app.post("/ask")
def ask_question(request: QuestionRequest):
    try:
        question = request.question.strip()

        if not question:
            raise HTTPException(
                status_code=400,
                detail="Question cannot be empty",
            )

        # Step 1: Embed the user's question
        print("Step 1: Embedding question...")
        question_embedding = create_embedding(question)

        # Step 2: Retrieve relevant document chunks
        print("Step 2: Searching FAISS...")
        relevant_chunks = search_chunks(question_embedding, top_k=3)

        if not relevant_chunks:
            raise HTTPException(
                status_code=404,
                detail="No relevant document content found",
            )

        # Step 3: Prepare retrieved context
        context = "\n\n".join(relevant_chunks)

        # Step 4: Generate the answer with Gemini
        print("Step 3: Generating answer...")
        answer = generate_answer(question, context)

        return {
            "question": question,
            "answer": answer,
            "retrieved_chunks": len(relevant_chunks),
        }

    except HTTPException:
        raise

    except Exception as exc:
        print("\nERROR DURING QUESTION ANSWERING")
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=f"{type(exc).__name__}: {exc}",
        ) from exc
