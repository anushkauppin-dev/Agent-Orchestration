import logging

logging.getLogger("transformers.tokenization_utils_base").setLevel(
    logging.ERROR
)



from transformers import AutoTokenizer

MODEL_NAME = "intfloat/e5-base-v2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)


def chunk_document(
    text: str,
    chunk_size: int = 400,
    overlap: int = 50
) -> list[str]:

    if not text or not text.strip():
        raise ValueError("Document text cannot be empty.")

    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk size.")

    # Tokenize the complete document without truncation
    token_ids = tokenizer(
    text,
    add_special_tokens=False,
    truncation=False
)["input_ids"]
    
    chunks = []
    start = 0

    while start < len(token_ids):
        end = start + chunk_size

        chunk_token_ids = token_ids[start:end]

        chunk_text = tokenizer.decode(
            chunk_token_ids,
            skip_special_tokens=True
        )

        if chunk_text.strip():
            chunks.append(chunk_text)

        if end >= len(token_ids):
            break

        start = end - overlap

    return chunks
