
from pathlib import Path

import pymupdf
from docx import Document


def extract_text_from_pdf(path: Path) -> str:
    extracted_text = []

    with pymupdf.open(path) as document:
        if document.page_count == 0:
            raise ValueError("The PDF document is empty.")

        for page in document:
            page_text = page.get_text("text")
            if page_text.strip():
                extracted_text.append(page_text)

    return "\n".join(extracted_text).strip()


def extract_text_from_docx(path: Path) -> str:
    document = Document(path)
    extracted_text = []

    # Extract paragraphs
    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            extracted_text.append(paragraph.text)

    # Extract table content
    for table in document.tables:
        for row in table.rows:
            row_text = " | ".join(
                cell.text.strip() for cell in row.cells
            )
            if row_text.strip():
                extracted_text.append(row_text)

    # Extract headers and footers
    for section in document.sections:
        for paragraph in section.header.paragraphs:
            if paragraph.text.strip():
                extracted_text.append(paragraph.text)

        for paragraph in section.footer.paragraphs:
            if paragraph.text.strip():
                extracted_text.append(paragraph.text)

    return "\n".join(extracted_text).strip()


def extract_text_from_document(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = path.suffix.lower()

    if extension == ".pdf":
        text = extract_text_from_pdf(path)

    elif extension == ".docx":
        text = extract_text_from_docx(path)

    else:
        raise ValueError(
            "Unsupported file format. Only PDF and DOCX are supported."
        )

    if not text:
        raise ValueError(
            "No readable text found in the document."
        )

    return text
