from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD_FILE: str

    FT_API_UID: str
    FT_API_SECRET: str
    FT_API_BASE_URL: str = "https://api.intra.42.fr/v2"
    FT_CAMPUS: str

    @property
    def POSTGRES_PASSWORD(self) -> str:
        return Path(self.POSTGRES_PASSWORD_FILE).read_text().strip()

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
