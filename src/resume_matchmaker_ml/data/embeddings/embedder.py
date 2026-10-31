from sentence_transformers import SentenceTransformer

MODEL_NAME = "intfloat/e5-base-v2"

model = SentenceTransformer(MODEL_NAME)


def generate_embeddings(
    texts: list[str],
    is_query: bool = False
) -> list[list[float]]:

    if not texts:
        return []

    if any(not text or not text.strip() for text in texts):
        raise ValueError("Texts cannot be empty.")

    prefix = "query: " if is_query else "passage: "

    prepared_texts = [
        prefix + text.strip()
        for text in texts
    ]

    embeddings = model.encode(
        prepared_texts,
        normalize_embeddings=True,
        show_progress_bar=True
    )

    return embeddings.tolist()