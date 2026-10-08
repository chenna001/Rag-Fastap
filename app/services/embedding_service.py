# import os

# from openai import OpenAI
# from dotenv import load_dotenv


# load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY")
# )


# def create_embedding(text: str) -> list[float]:

#     response = client.embeddings.create(
#         model="text-embedding-3-small",
#         input=text
#     )

#     return response.data[0].embedding

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# import os

# from dotenv import load_dotenv
# from google import genai


# load_dotenv()

# client = genai.Client(
#     api_key=os.getenv("GOOGLE_API_KEY")
# )


# def create_embedding(text: str) -> list[float]:

#     response = client.models.embed_content(
#         model="gemini-embedding-2",
#         contents=text
#     )

#     return response.embeddings[0].values

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ new code add
import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    raise ValueError("GOOGLE_API_KEY is missing from .env")


client = genai.Client(
    api_key=google_api_key
)


def create_embedding(text: str) -> list[float]:

    response = client.models.embed_content(
        model="gemini-embedding-2",
        contents=text
    )

    return response.embeddings[0].values