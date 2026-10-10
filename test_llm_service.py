
from app.services.llm_service import generate_answer

question = "What is RAG?"
context = """
RAG stands for Retrieval-Augmented Generation.
It retrieves relevant information from documents
and uses that information to generate answers.
"""

try:
    answer = generate_answer(question, context)
    print("Question:", question)
    print("Answer:", answer)
except Exception as error:
    print("Test failed:", error)
