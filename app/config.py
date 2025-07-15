import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_USER: str 
    DB_PASSWORD: str 
    DB_HOST: str 
    DB_PORT: int 
    DB_NAME: str 
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_LIFETIME: int
    REFRESH_TOKEN_LIFETIME: int
    REFRESH_SECRET_KEY: str

    class Config:
        env_file = ".env"
        
    @property
    def get_db_uri(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()

DATABASE_URL = settings.get_db_uri

