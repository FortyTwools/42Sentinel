from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # DATABASE_URL: str
    FT_API_UID: str
    FT_API_SECRET: str
    FT_API_BASE_URL: str = "https://api.intra.42.fr/v2"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
