from aiogram import types, Dispatcher
from aiogram.dispatcher.storage import FSMContext

from states.states import DateWeather
from external_services.weather import WeatherClient
from lexicon.lexicon_ru import MessageSelector, ImagesSelector


def register_privat_user_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(send_command_start_user, commands=['start', 'старт', "Старт"])
    dp.register_message_handler(send_command_help_user, commands=['help', "помощь", "Помощь"])
    dp.register_message_handler(post_city_from_bot, commands=["weather", "погода"])
    dp.register_message_handler(send_weather, state=DateWeather.City)


# Commad Start from user
async def send_command_start_user(message: types.Message):
    img = ImagesSelector()
    msg = MessageSelector()
    await message.bot.send_animation(
        chat_id=message.chat.id,
        animation=img.random_img("hello"),
        caption=msg.message_user("hello"))
    await message.delete()


async def send_command_help_user(message: types.Message):
    img = ImagesSelector()
    msg = MessageSelector()
    await message.bot.send_animation(
        chat_id=message.chat.id,
        animation=img.random_img("help"),
        caption=msg.message_user("help"))
    await message.delete()


# commnad /weather
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
        if weather_data:
            img = ImagesSelector.random_img(weather_description, "other")
            await message.bot.send_animation(
                chat_id=message.chat.id,
                animation=img,
                caption=weather.message_format_tg(),
            )
            await state.reset_state()
    except Exception as e:
        await message.bot.send_message(
            chat_id=message.chat.id,
            text=("<b>Вы не правильно ввели название города. </b>"
                  "<b>Повторите команду /weather, для получения погоды</b>"))
        await state.reset_state()
