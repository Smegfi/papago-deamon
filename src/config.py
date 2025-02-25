import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_URL = str(os.getenv("PAPAGO_API_URL"))
    TIMEOUT = int(os.getenv("PAPAGO_TIMEOUT"))
    if not API_URL:
        raise ValueError("PAPAGO_API_URL is not set")
    if not TIMEOUT:
        TIMEOUT = 7


