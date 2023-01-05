from pydantic import BaseModel
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Settings(BaseModel):
# Database
    DB_HOST: str = os.getenv('DB_HOST')
    DB_PORT: str = os.getenv('DB_PORT')
    DB_DATABASE: str = os.getenv('DB_DATABASE')
    DB_TYPE: str = os.getenv('DB_TYPE')
    DB_USER: str = os.getenv('DB_USER')
    DB_PASSWORD: str = os.getenv('DB_PASSWORD')

    # API
    API_PORT: str = os.getenv('API_PORT')
    JWT_SECRET_KEY: str = os.getenv('JWT_SECRET_KEY')
    JWT_REFRESH_SECRET_KEY: str = os.getenv('JWT_REFRESH_SECRET_KEY')
    JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM')

def get_config() -> Settings:
    return Settings()