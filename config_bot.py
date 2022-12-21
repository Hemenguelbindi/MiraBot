import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))


admins = [
    int(os.getenv("BINDI_ADMIN_ID")),
    int(os.getenv("KRIS_ADMIN_ID")),
    ]

#  vip person
admin_hemen = int(os.getenv("BINDI_ADMIN_ID"))
admin_kris = int(os.getenv("KRIS_ADMIN_ID"))

# token weather 
OPEN_WEATHER = str(os.getenv("TOKEN_API_WEATHER"))

# setting telegam client

CONNECT_LINK = "https://api.telegram.org"