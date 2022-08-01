import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [
    int(os.getenv("BINDI_ADMIN_ID")),
    int(os.getenv("KRIS_ADMIN_ID")),
]


OPEN_WEATHER = str(os.getenv("TOKEN_API_WEATHER"))
