
from resume_matchmaker_ml.extraction.document_extractor import (
    extract_text_from_document
)
from resume_matchmaker_ml.data.embeddings.chunker import (
    chunk_document,
    tokenizer
)
from resume_matchmaker_ml.data.embeddings.embedder import generate_embeddings
from resume_matchmaker_ml.data.embeddings.embedding_storage import save_embeddings


DOCUMENTS = [
    {
        "path": r"C:\Users\Anushka\OneDrive\Documents\Employer_Job_Description_Junior_Python_Developer.docx",
        "document_id": "job_junior_python_developer",
        "document_type": "job_description",
    },
    {
        "path": r"C:\Users\Anushka\OneDrive\Documents\Sample_Candidate_Resume.docx",
        "document_id": "candidate_001",
        "document_type": "resume",
    },
]

MAX_TOKENS = 512

for document in DOCUMENTS:
    print(f"\nPROCESSING: {document['path']}")

    # 1. Extract complete document text
    document_text = extract_text_from_document(document["path"])

    # 2. Create token-aware chunks
    chunks = chunk_document(
        document_text,
        chunk_size=400,
        overlap=50
    )

    print("Total chunks:", len(chunks))

    # 3. Verify token count of every chunk
    token_counts = [
        len(tokenizer.encode(chunk, add_special_tokens=True))
        for chunk in chunks
    ]

    print("Token count per chunk:", token_counts)

    assert all(
        count <= MAX_TOKENS for count in token_counts
    ), "A chunk exceeds the model's 512-token limit!"

    print("Token limit verification successful!")

    # 4. Generate embeddings
    embeddings = generate_embeddings(chunks, is_query=False)

    print("Total embeddings:", len(embeddings))
    print("Embedding dimensions:", len(embeddings[0]))

    assert len(embeddings) == len(chunks)
    assert all(len(vector) == 768 for vector in embeddings)

    # 5. Save embeddings and their associated text
    saved_path = save_embeddings(
        chunks=chunks,
        embeddings=embeddings,
        document_id=document["document_id"],
        document_type=document["document_type"]
    )

    print("Saved successfully at:", saved_path)

print("\nALL DOCUMENTS PROCESSED SUCCESSFULLY!")
