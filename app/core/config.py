from pydantic.v1 import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    #database configuration
    DB_URL = os.getenv("ASYNC_DATABASE_URL")
    #security
    SECRET_KEY = os.getenv("SECRET_KEY")

settings = Settings()