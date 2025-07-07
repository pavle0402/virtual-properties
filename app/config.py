import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_USER: str 
    DB_PASSWORD: str 
    DB_HOST: str 
    DB_PORT: int 
    DB_NAME: str 

    class Config:
        env_file = ".env"
        
    @property
    def get_db_uri(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()

DATABASE_URL = settings.get_db_uri

