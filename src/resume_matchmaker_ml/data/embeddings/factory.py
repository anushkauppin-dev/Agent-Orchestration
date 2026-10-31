from .openai_provider import OpenAIEmbeddingProvider

def get_embedding_provider():
    # Add Gemini or Sentence Transformers adapters here without changing callers.
    return OpenAIEmbeddingProvider()
