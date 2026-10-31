
from resume_matchmaker_ml.extraction.document_extractor import (
    extract_text_from_document
)
from resume_matchmaker_ml.data.embeddings.chunker import chunk_document


# Add your actual PDF and DOCX paths here
DOCUMENT_PATHS = [
    r"C:\Users\Anushka\OneDrive\Documents\Employer_Job_Description_Junior_Python_Developer.docx",
    r"C:\Users\Anushka\OneDrive\Documents\Sample_Candidate_Resume.docx"
]


for document_path in DOCUMENT_PATHS:

    print(f"\nPROCESSING: {document_path}")

    # Extract complete document text
    document_text = extract_text_from_document(document_path)

    # Create chunks from the complete extracted text
    chunks = chunk_document(
        document_text,
        chunk_size=350,
        overlap=50
    )

    print("TOTAL WORDS:", len(document_text.split()))
    print("TOTAL CHUNKS:", len(chunks))

    for index, chunk in enumerate(chunks, start=1):
        print(f"\n--- CHUNK {index} ---")
        print(chunk)
