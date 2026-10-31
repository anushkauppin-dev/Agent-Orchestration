from src.resume_matchmaker_ml.client import grok_client, EMBEDDING_MODEL


def generate_embedding(text: str) -> list[float]:
    response = grok_client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )

    return response.data[0].embedding