from pathlib import Path
import fitz
from docx import Document

SUPPORTED = {".pdf", ".docx"}

def extract_text(path: Path) -> str:
    """Extract text from a PDF or DOCX. Scanned PDFs need OCR fallback."""
    path = Path(path)
    suffix = path.suffix.lower()
    if suffix not in SUPPORTED:
        raise ValueError(f"Unsupported file type: {suffix}")

    if suffix == ".pdf":
        with fitz.open(path) as pdf:
            pages = [page.get_text("text") for page in pdf]
        text = "\n".join(pages).strip()
        if not text:
            raise ValueError("No selectable text found; this may be a scanned PDF. Run OCR.")
        return text

    doc = Document(path)
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    table_text = []
    for table in doc.tables:
        for row in table.rows:
            table_text.append(" | ".join(cell.text.strip() for cell in row.cells))
    return "\n".join(paragraphs + table_text).strip()
