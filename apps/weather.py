import asyncio
import datetime
import httpx

from configs_apps.config_weather import OPEN_WEATHER


async def get_weather(city, token):
    try:
        r = httpx.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric")
        data = r.json()
        city = data["name"]
        temp_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_times = datetime.datetime.fromtimestamp(data['sys']["sunrise"])
        sunset_times = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = sunset_times - sunrise_times
        weather_discriotion = data["weather"][0]["main"]
        print(f"***{datetime.datetime.now().strftime('%H:%M %d-%m-%Y')}***\n"
              f"Погода в городе: {city}\nТемпература:{temp_weather}С° {weather_discriotion}\n"
              f"Влажность: {humidity}\nДавление:{pressure}мм.рт.ст\nВетер: {wind} м/с\n"
              f"Восход солнца: {sunrise_times}\nЗаход солнца:{sunset_times}\n"
              f'Продолжительность светового дня {length_of_the_day}\n Хорошего дня!'
              )

    except Exception as ex:
        print(ex)
        print("Проверьте название города")


async def main():
    city = input("Название города: ")
    await get_weather(city, OPEN_WEATHER)


if __name__ == "__main__":
    asyncio.run(main())
