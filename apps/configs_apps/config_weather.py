import os

from dotenv import load_dotenv

load_dotenv()

OPEN_WEATHER = str(os.getenv("TOKEN_API_WEATHER"))
