from datetime import datetime

from aiogram import Bot

from loguru import logger

from lexicon import choise_random_gif, active_and_care
from config_data.config import get_admins
from external_services.weather import WeatherClient


async def send_weather(bot: Bot):
    for admin in get_admins():
        try:
            weather = WeatherClient(city="Уфа")
            weather_data = weather.ask_data()
            weather_description = weather_data["weather"][0]["main"]
            match weather_description:
                case "Clouds":
                    await bot.send_animation(
                        chat_id=admin,
                        animation=choise_random_gif("clouds"),
                        caption=weather.message_format_tg(),
                    )
                case "Rain":
                    await bot.send_animation(
                        chat_id=admin,
                        animation=choise_random_gif("rain"),
                        caption=weather.message_format_tg()
                    )
                case "Thunderstorm":
                    await bot.send_animation(
                        chat_id=admin,
                        animation=choise_random_gif("thunderstorm"),
                        caption=weather.message_format_tg(),
                    )
                case "Snow":
                    await bot.send_animation(
                        chat_id=admin,
                        animation=choise_random_gif("snow"),
                        caption=weather.message_format_tg(),
                    )
                case "Clear":
                    await bot.send_animation(
                        chat_id=admin,
                        animation=choise_random_gif("thunderstorm"),
                        caption=weather.message_format_tg(),
                    )
                case _:
                    await bot.send_animation(
                        chat_id=admin,
                        animation=choise_random_gif("other"),
                        caption=weather.message_format_tg(),
                    )
        except Exception as e:
            logger.error(e)


async def send_active_care(bot: Bot):
    admin_krist = get_admins()[1]
    to_day = datetime.today().strftime("%d.%m.%Y")
    get_active = active_and_care.get(to_day)
    if get_active is not None:
        await bot.send_message(admin_krist, text=get_active)
