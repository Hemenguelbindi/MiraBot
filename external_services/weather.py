import datetime
import httpx
from loguru import logger
from .config_api import load_config_api, ConfigAPI


config_weather: ConfigAPI = load_config_api()

class WeatherClient:
    def __init__(self, city: str, base_url:str = config_weather.base_url_weather, token:str = config_weather.weath_token)->None:
        self.base_url: str = base_url
        self.token: str = token
        self.city: str = city
        self.default_params: dict = {"q": self.city, "appid": self.token, "units":"metric"}      
    
    def message_in_console(self) -> str:
        data: dict = self.ask_data()
        weather_description: str = data["weather"][0]["main"]
        city: str = data["name"]
        temp_weather: str = data["main"]["temp"]
        humidity: str = data["main"]["humidity"]
        pressure: str = data["main"]["pressure"]
        wind: str = data["wind"]["speed"]
        sunrise_times: str = datetime.datetime.fromtimestamp(data['sys']["sunrise"])
        sunset_times: str = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day: str = sunset_times - sunrise_times
        return (f"***{datetime.datetime.now().strftime('%H:%M %d-%m-%Y')}***\n"
                f"Погода в городе: {city}\nТемпература:{temp_weather}С {weather_description}°\n"
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
        return ( f"<b>***{datetime.datetime.now().strftime('%H:%M %d-%m-%Y')}***\n</b>"
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
            logger.error(e)
            

if __name__ == "__main__":
    w = WeatherClient(city="Москва")
    print(w.message_in_console())