import datetime

import httpx

from loguru import logger

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.storage import FSMContext

from loader import dp, mira

from states import DateWeather
from configurations.config import OPEN_WEATHER, CONNECT_LINK


@dp.message_handler(Command("weather"))
async def post_city_from_bot(message: types.Message):
    await message.answer("Введите название города на кирилице или латинице например: Moscow, Саратов")
    await DateWeather.City.set()


@dp.message_handler(state=DateWeather.City)
async def send_weather(message: types.Message, state: FSMContext):
    city = message.text
    await state.update_data(city=city)

    clouds = types.InputFile(path_or_bytesio="photos/weather/Clouds.gif")
    rain = types.InputFile(path_or_bytesio="photos/weather/Rain.gif")
    thunderstorm = types.InputFile(path_or_bytesio="photos/weather/Thunderstorm.gif")
    snow = types.InputFile(path_or_bytesio="photos/weather/Snow.gif")
    clear = types.InputFile(path_or_bytesio="photos/weather/Clear.gif")
    atmosphere = types.InputFile(path_or_bytesio="photos/weather/Atmosphere.gif")

    try:
        request = httpx.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPEN_WEATHER}&units=metric"
            )
        data = request.json()

        city = data["name"]
        weather_description = data["weather"][0]["main"]
        temp_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_times = datetime.datetime.fromtimestamp(data['sys']["sunrise"])
        sunset_times = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = sunset_times - sunrise_times
        summary_weather = (
                 f"<b>***{datetime.datetime.now().strftime('%H:%M %d-%m-%Y')}***\n</b>"
                 f"<b>Погода в городе: {city}\nТемпература:{temp_weather}С° {weather_description}\n</b>"
                 f"<b>Влажность: {humidity}\nДавление:{pressure}мм.рт.ст\nВетер: {wind} м/с\n</b>"
                 f"<b>Восход солнца: {sunrise_times}\nЗаход солнца:{sunset_times}\n</b>"
                 f"<b>Продолжительность светового дня {length_of_the_day}\n Хорошего дня!</b>")

        if weather_description == "Clouds":
            await mira.send_animation(
                chat_id=message.chat.id,
                animation=clouds,
                caption=summary_weather,
                )
            await state.reset_state()

        elif weather_description == "Rain":
            await mira.send_animation(
                chat_id=message.chat.id,
                animation=rain,
                caption=summary_weather
                )
            await state.reset_state()

        elif weather_description == "Thunderstorm":
            await mira.send_animation(
                chat_id=message.chat.id,
                animation=thunderstorm,
                caption=summary_weather,
                )
            await state.reset_state()

        elif weather_description == "Snow":
            await mira.send_animation(
                chat_id=message.chat.id,
                animation=snow,
                caption=summary_weather,
                )
            await state.reset_state()

        elif weather_description == "Clear":
            await mira.send_animation(
                chat_id=message.chat.id,
                animation=clear,
                caption=summary_weather,
                )
            await state.reset_state()

        elif weather_description in [
                                     "Mist",
                                     "Smoke",
                                     "Haze",
                                     "Dust",
                                     "Fog",
                                     "Sand",
                                     "Dust",
                                     "Ash",
                                     "Squall",
                                     "Tornado"
                                     ]:
            await mira.send_animation(
                chat_id=message.chat.id,
                animation=atmosphere,
                caption=summary_weather,
                )
            await state.reset_state()

    except Exception as ex:
        logger.error(ex)
        logger.info("Проверьте название города")
        await mira.send_message(
            chat_id=message.chat.id,
            text=("<b>Вы не правильно ввели название города. </b>"
                  "<b>Повторите команду /weather, для получения погоды</b>"
                  ))
        await state.reset_state()
        r = httpx.post(f"{CONNECT_LINK}{datetime.datetime.now()}||{ex.__class__}||{ex}")
        
        