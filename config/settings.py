"""
Configuration settings for API testing
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """
    Application settings
    """
    BASE_URL = os.getenv("BASE_URL", "https://fakestoreapi.com")
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "10"))

    MAX_RESPONSE_TIME_MS = int(os.getenv("MAX_RESPONSE_TIME_MS", "3000"))

settings = Settings()