import json
from aiogram.dispatcher.storage import FSMContext
from aiogram import types, Dispatcher
from states.states import DateWeather

from loguru import logger
from lexicon import random_hello_user,  help_text, choise_random_gif
from external_services.weather import WeatherClient




def register_user_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(send_command_start_user, commands=['start', 'старт', "Старт"])
    dp.register_message_handler(send_command_help_user, commands=['help', "помощь", "Помощь"])
    dp.register_message_handler(post_city_from_bot, commands=["weather", "погода"])
    dp.register_message_handler(send_weather, state=DateWeather.City)


# Commad Start from user
async def send_command_start_user(message: types.Message):
    await message.bot.send_animation(
                chat_id=message.chat.id,
                animation=choise_random_gif("hello"),                     
                caption=random_hello_user)
   
# Commad Help from user
async def send_command_help_user(message: types.Message):
   await message.bot.send_animation(
                chat_id=message.chat.id,
                animation=choise_random_gif("help"),                     
                caption=help_text)
   await message.delete()


# command /weather
async def post_city_from_bot(message: types.Message):
    await message.answer("Введите название города на кирилице или латинице например: Moscow, Саратов")
    await DateWeather.City.set()


async def send_weather(message: types.Message, state: FSMContext):
    
    city = message.text
    await state.update_data(city=city)
    try:
        weather = WeatherClient(city=city)
        weather_data = weather.ask_data()
        weather_description = weather_data["weather"][0]["main"]
        
        match weather_description:
            case "Clouds":
                await message.bot.send_animation(
                chat_id=message.chat.id,
                animation=choise_random_gif("clouds"),
                caption=weather.message_format_tg(),
                )
                await state.reset_state()            
            case "Rain":
                await message.bot.send_animation(
                chat_id=message.chat.id,
                animation=choise_random_gif("rain"),
                caption=weather.message_format_tg()
                )
                await state.reset_state()            
            case "Thunderstorm":
                await message.bot.send_animation(
                chat_id=message.chat.id,
                animation=choise_random_gif("thunderstorm"),
                caption=weather.message_format_tg(),
                )
                await state.reset_state()            
            case "Snow":
                await message.bot.send_animation(
                chat_id=message.chat.id,
                animation=choise_random_gif("snow"),
                caption=weather.message_format_tg(),
                )
                await state.reset_state()              
            case "Clear":
                await message.bot.send_animation(
                chat_id=message.chat.id,
                animation=choise_random_gif("thunderstorm"),
                caption=weather.message_format_tg(),
                )
                await state.reset_state()
            case _ :
                await message.bot.send_animation(
                chat_id=message.chat.id,
                animation=choise_random_gif("other"),
                caption=weather.message_format_tg(),
                )
                await state.reset_state()               
    except Exception as e:
        logger.error(e)
        await message.bot.send_message(
                chat_id=message.chat.id,
                text=("<b>Вы не правильно ввели название города. </b>"
                    "<b>Повторите команду /weather, для получения погоды</b>"))
        await state.reset_state()
