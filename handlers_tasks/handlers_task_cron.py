from aiogram import Bot

from loguru import logger

from config_data.config import get_admins
from external_services.weather import WeatherClient
from lexicon.lexicon_ru import MessageSelector, ImagesSelector, LinkLessonSelector


async def send_weather(bot: Bot):
    for admin in get_admins():
        try:
            weather = WeatherClient(city="Уфа")
            weather_data = weather.ask_data()
            weather_description = weather_data["weather"][0]["main"]

            if weather_data:
                animation_weather = ImagesSelector().random_img(weather_description)
                await bot.send_animation(
                    chat_id=admin,
                    animation=animation_weather,
                    caption=weather.message_format_tg(),
                )
        except Exception as e:
            logger.error(e)


async def random_workout(bot: Bot):
    admin = get_admins()
    img = ImagesSelector().random_img("sport")
    msg = MessageSelector().message_workout()
    await bot.send_animation(
        chat_id=admin[1],
        animation=img,
        caption=msg,
    )


async def time_learn(bot: Bot):
    admin = get_admins()
    img = ImagesSelector().random_img("just_learn")
    link = LinkLessonSelector()
    if link is not None:
        await bot.send_animation(
            chat_id=admin[1],
            animation=img,
            caption=link.lesson_link(),
        )
