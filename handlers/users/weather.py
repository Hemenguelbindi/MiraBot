import datetime

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.storage import FSMContext

from loader import dp, mira

from states import DateWeather

from message_exept import create_error_message

from config_bot import OPEN_WEATHER, CONNECT_LINK, admin_hemen

from weather_app.weather import WeatherClient


def message_weather(city:str, temp_weather: str, weather_description:str, humidity: str, pressure: str, wind:str,sunrise_times: str, sunset_times: str, length_of_the_day)-> str:
    """_str_

    Args:
        city (str): название города
        temp_weather (str): температура воздуха 
        weather_description (str): заголовок погоды
        humidity (str): влажность
        pressure (str): давление
        wind (str): сила ветра
        sunrise_times (str): время от начала дня
        sunset_times (str):  время конца дня 
        length_of_the_day (_type_): общая продолжительность светового дня

    Returns:
        str: _фарматированное соощение полностью_
    """    
    return (
                 f"<b>***{datetime.datetime.now().strftime('%H:%M %d-%m-%Y')}***\n</b>"
                 f"<b>Погода в городе: {city}\nТемпература:{temp_weather}С° {weather_description}\n</b>"
                 f"<b>Влажность: {humidity}\nДавление:{pressure}мм.рт.ст\nВетер: {wind} м/с\n</b>"
                 f"<b>Восход солнца: {sunrise_times}\nЗаход солнца:{sunset_times}\n</b>"
                 f"<b>Продолжительность светового дня {length_of_the_day}\n Хорошего дня!</b>")

# Command weather 
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
        weather = WeatherClient(city=city)
        weather_data = weather.ask_data()
        weather_description = weather_data["weather"][0]["main"]
        
        match weather_description:
            
            case "Clouds":
                await mira.send_animation(
                chat_id=message.chat.id,
                animation=clouds,
                caption=weather.message_format_tg(),
                )
                await state.reset_state()
            
            case "Rain":
                await mira.send_animation(
                chat_id=message.chat.id,
                animation=rain,
                caption=weather.message_format_tg()
                )
                await state.reset_state()
            
            case "Thunderstorm":
                await mira.send_animation(
                chat_id=message.chat.id,
                animation=thunderstorm,
                caption=weather.message_format_tg(),
                )
                await state.reset_state()
            
            case "Snow":
                await mira.send_animation(
                chat_id=message.chat.id,
                animation=snow,
                caption=weather.message_format_tg(),
                )
                await state.reset_state()
                
            case "Clear":
                await mira.send_animation(
                chat_id=message.chat.id,
                animation=clear,
                caption=weather.message_format_tg(),
                )
                await state.reset_state()
            
            case _ :
                await mira.send_animation(
                chat_id=message.chat.id,
                animation=atmosphere,
                caption=weather.message_format_tg(),
                )
                await state.reset_state()
                

    except Exception as e:
        await mira.send_message(
            chat_id=message.chat.id,
            text=("<b>Вы не правильно ввели название города. </b>"
                  "<b>Повторите команду /weather, для получения погоды</b>"))
        await state.reset_state()
        mira.telegram_client.post(method="sendMessange", 
                                  params={"text":create_error_message(e), 
                                            "chat_id":admin_hemen})
