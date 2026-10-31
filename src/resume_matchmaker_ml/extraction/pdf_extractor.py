
import pymupdf
from pathlib import Path


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract readable text from a PDF document.
    """

    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError("Only PDF files are supported.")

    extracted_text = []

    with pymupdf.open(path) as document:
        if document.page_count == 0:
            raise ValueError("The PDF document is empty.")

        for page_number, page in enumerate(document, start=1):
            page_text = page.get_text("text")

            if page_text.strip():
                extracted_text.append(page_text)

    full_text = "\n".join(extracted_text).strip()

    if not full_text:
        raise ValueError(
            "No readable text found. This may be a scanned PDF "
            "that requires OCR."
        )

    return full_text
