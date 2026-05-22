from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DATABASE_URL: str
    MODEL_NAME: str
    OLLAMA_BASE_URL: str
    VECTOR_DB_PATH: str

    class Config:
        env_file = ".env"


settings = Settings()