
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai


# Load .env from the project root
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)

# Read the API key used by embedding_service.py
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise RuntimeError(
        "GOOGLE_API_KEY is missing from the project .env file"
    )

client = genai.Client(api_key=api_key)


def generate_answer(question: str, context: str) -> str:
    """Generate an answer using retrieved RAG context."""

    prompt = f"""
You are a helpful AI assistant.

Answer the question using only the context below.
If the answer is not present in the context,
say that you do not have enough information.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    answer = response.text

    if not answer:
        raise RuntimeError("The AI model returned an empty response.")

    return answer
