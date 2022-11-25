import datetime
import httpx

from loader import mira

from  message_exept import create_error_message
from config_bot import admins
from .config_weather import OPEN_WEATHER, API_WEATHER


class WeatherClient:
    def __init__(self, base_url:str = API_WEATHER, token:str = OPEN_WEATHER, city: str = "Уфа"):
        self.base_url = base_url
        self.token = token
        self.city = city
        self.default_params = {"q": self.city, "appid": self.token, "units":"metric"}      
    
    def message_in_console(self) -> str:
        data = self.ask_data()
        weather_description = data["weather"][0]["main"]
        city = data["name"]
        temp_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_times = datetime.datetime.fromtimestamp(data['sys']["sunrise"])
        sunset_times = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = sunset_times - sunrise_times
        return (f"***{datetime.datetime.now().strftime('%H:%M %d-%m-%Y')}***\n"
                f"Погода в городе: {city}\nТемпература:{temp_weather}С°\n"
                f"Влажность: {humidity}\nДавление:{pressure}мм.рт.ст\nВетер: {wind} м/с\n"
                f"Восход солнца: {sunrise_times}\nЗаход солнца:{sunset_times}\n"
                f'Продолжительность светового дня {length_of_the_day}\n Хорошего дня!')
              
    def message_format_tg(self)-> str:
        data = self.ask_data()
        weather_description = data["weather"][0]["main"]
        city = data["name"]
        temp_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_times = datetime.datetime.fromtimestamp(data['sys']["sunrise"])
        sunset_times = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = sunset_times - sunrise_times
        return (
                 f"<b>***{datetime.datetime.now().strftime('%H:%M %d-%m-%Y')}***\n</b>"
                 f"<b>Погода в городе: {city}\nТемпература:{temp_weather}С° {weather_description}\n</b>"
                 f"<b>Влажность: {humidity}\nДавление:{pressure}мм.рт.ст\nВетер: {wind} м/с\n</b>"
                 f"<b>Восход солнца: {sunrise_times}\nЗаход солнца:{sunset_times}\n</b>"
                 f"<b>Продолжительность светового дня {length_of_the_day}\n Хорошего дня!</b>")
    
    def ask_data(self, params: dict = None, body: dict = None)->dict :
        try:
            if params is None:
                params = self.default_params
                with httpx.Client() as client:
                    rep = client.post(self.base_url, params=params, data=body)
                    return rep.json() 
        except Exception as e:
            mira.telegram_client.post(method="sendMessange", 
                                    params={"text":create_error_message(e), 
                                            "chat_id":admins[0]})
            
    

if __name__ == "__main__":
    w = WeatherClient("Уфа")
    print(w.message_in_console())