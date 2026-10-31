def extract_scanned_pdf_text(file_path: str) -> str:
    """OCR extension point.

    Install Tesseract and a PDF-to-image package (for example, pytesseract +
    pdf2image) before implementing this adapter. Keep OCR separate from normal
    text extraction and record that OCR was used in document metadata.
    """
    raise NotImplementedError("Configure Tesseract OCR to process scanned PDFs.")
