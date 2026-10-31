from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    llm_provider: str = "openai"
    openai_api_key: str = ""
    openai_chat_model: str = "gpt-4.1-mini"
    embedding_provider: str = "openai"
    openai_embedding_model: str = "text-embedding-3-small"
    embedding_dimensions: int = 1536

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
