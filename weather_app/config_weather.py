import os

from dotenv import load_dotenv

load_dotenv()


API_WEATHER = "https://api.openweathermap.org/data/2.5/weather"
OPEN_WEATHER = str(os.getenv("TOKEN_API_WEATHER"))
