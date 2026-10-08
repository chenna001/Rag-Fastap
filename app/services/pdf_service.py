from pypdf import PdfReader
from io import BytesIO


def extract_text(pdf_bytes: bytes) -> str:
    """
    Extract text from a PDF file.

    Args:
        pdf_bytes: PDF file content as bytes

    Returns:
        Extracted text as a string
    """

    reader = PdfReader(BytesIO(pdf_bytes))

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text