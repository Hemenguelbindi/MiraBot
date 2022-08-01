from loguru import logger


from aiogram import Dispatcher

from data.config import admins


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "Я готова работать, хозяин!")
        except Exception as err:
            logger.error(err)
