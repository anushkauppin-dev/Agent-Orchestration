from openai import OpenAI
from ..config import settings

class OpenAIEmbeddingProvider:
    def __init__(self):
        if not settings.openai_api_key:
            raise RuntimeError("Set OPENAI_API_KEY in your .env file.")
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_embedding_model

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            return []
        result = self.client.embeddings.create(
            model=self.model,
            input=texts,
            dimensions=settings.embedding_dimensions
        )
        return [item.embedding for item in result.data]
