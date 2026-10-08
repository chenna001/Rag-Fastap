# RAG-FastAPI

A **Retrieval-Augmented Generation (RAG)** application built with **Python, FastAPI, LLMs, embeddings, and vector search**.

The application allows users to upload PDF documents and ask questions based on the document content. The RAG pipeline retrieves relevant information from the uploaded documents and provides context to the LLM to generate an accurate answer.

## Project Overview

This project demonstrates how to build a RAG application from scratch using FastAPI.

### RAG Architecture

```text
User
  |
  v
FastAPI
  |
  +---- Upload PDF
  |        |
  |        v
  |    PDF Text Extraction
  |        |
  |        v
  |    Text Chunking
  |        |
  |        v
  |    Embeddings
  |        |
  |        v
  |    Vector Database
  |
  +---- Ask Question
           |
           v
      Query Embedding
           |
           v
      Similarity Search
           |
           v
     Relevant Documents
           |
           v
      Context + Question
           |
           v
          LLM
           |
           v
         Answer
```

## Technologies

* Python
* FastAPI
* Uvicorn
* PyPDF
* OpenAI LLM
* OpenAI Embeddings
* LangChain
* FAISS
* Pydantic
* Python-dotenv
* REST API
* Swagger / OpenAPI

## Project Structure

```text
Rag-Fastap/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   └── services/
│       ├── __init__.py
│       └── pdf_service.py
│
├── data/
│   └── documents/
│
├── .gitignore
├── environment.yml
├── LICENSE
└── README.md
```

## Features

### Current Features

* FastAPI application
* PDF upload API
* PDF text extraction
* Swagger API documentation
* Modular service structure

### Planned Features

* Text chunking
* Text embeddings
* FAISS vector database
* Semantic similarity search
* LLM integration
* Complete RAG question-answering API
* Conversation history
* Error handling
* Logging
* Docker deployment
* Authentication
* Production deployment

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Rag-Fastap
```

### 2. Create a Python environment

Using Conda:

```bash
conda env create -f environment.yml
```

Activate the environment:

```bash
conda activate rag-fastapi
```

### 3. Install dependencies

If using a virtual environment instead of Conda:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_openai_api_key
```

Do not commit `.env` to GitHub.

Add this to `.gitignore`:

```text
.env
.venv/
__pycache__/
*.pyc
```

## Run the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

## Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

FastAPI automatically provides interactive Swagger documentation.

## API Endpoints

### Home

```text
GET /
```

Example response:

```json
{
  "message": "RAG AI Assistant is running"
}
```

### Upload PDF

```text
POST /upload
```

Upload a PDF document using the `file` parameter.

Example response:

```json
{
  "filename": "sample.pdf",
  "text_length": 2450,
  "text_preview": "Extracted text from the PDF..."
}
```

## RAG Pipeline

The complete RAG pipeline will follow these steps:

### Step 1: Document Upload

The user uploads a PDF through the FastAPI endpoint.

### Step 2: Text Extraction

PyPDF extracts text from each PDF page.

### Step 3: Text Chunking

The extracted text is divided into smaller chunks.

Example:

```text
Large Document
      |
      v
Chunk 1
Chunk 2
Chunk 3
Chunk 4
```

### Step 4: Embeddings

Each text chunk is converted into a numerical vector using an embedding model.

```text
Text
  |
  v
Embedding Model
  |
  v
Vector
```

### Step 5: Vector Search

The vectors are stored in FAISS and used for similarity search.

### Step 6: Retrieval

When the user asks a question, the question is converted into an embedding and compared with stored document vectors.

### Step 7: LLM Generation

The retrieved document chunks are provided to the LLM as context.

```text
Question
   +
Retrieved Context
   |
   v
   LLM
   |
   v
Answer
```

## Example Use Case

A user uploads:

```text
company_policy.pdf
```

Then asks:

```text
What is the company's leave policy?
```

The application:

1. Converts the question into an embedding.
2. Searches the vector database.
3. Retrieves relevant document chunks.
4. Sends the question and retrieved context to the LLM.
5. Returns the generated answer.

## Future Enhancements

* Multiple document support
* Metadata filtering
* Advanced chunking strategies
* Hybrid search
* Reranking
* Conversation memory
* Streaming LLM responses
* PostgreSQL integration
* Redis caching
* Docker
* Kubernetes
* Cloud deployment
* Monitoring and logging
* Authentication and authorization

## Learning Objectives

This project is designed to demonstrate practical experience with:

* Python
* FastAPI
* REST APIs
* PDF processing
* Text processing
* Embeddings
* Vector databases
* Semantic search
* RAG architecture
* LLM integration
* AI application development

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

**Chennakesava Reddy**

AI / LLM Engineer
Python | FastAPI | RAG | LLMs | LangChain | Vector Databases
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  GOOGLE API        @@@@@@@@@@@@@@@@
## Google Gemini API

This project uses the Google Gemini API for:

* Text embeddings
* Vector-based semantic search
* LLM-based question answering

### Embedding Model

The project uses:

```text
gemini-embedding-2
```

The embedding model converts text chunks into numerical vectors for semantic search.

Current embedding dimension:

```text
3072
```

### API Key Configuration

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
```

For local development, load the API key using `python-dotenv`.

**Important:** Never commit the `.env` file or expose the API key in GitHub.

The `.gitignore` file includes:

```text
.env
**/.env
```

### Security

* Never hard-code API keys in Python files.
* Never add API keys to `README.md`.
* Never commit `.env` to GitHub.
* If an API key is accidentally exposed, revoke it and create a new key.

* 
Author
Chennakesava Reddy
www.linkedin.com/in/chennakeava-reddy-reddy-35a43ba5
AI / LLM Engineer Python | FastAPI | RAG | LLMs | LangChain | Vector Databases
