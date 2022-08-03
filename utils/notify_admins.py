from loguru import logger


from aiogram import Dispatcher

from configurations.config import admins


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(admins[0], "Я готова работать, хозяин!")
    except Exception as err:
        logger.error(err)
