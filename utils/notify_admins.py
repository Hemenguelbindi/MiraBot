from aiogram import Dispatcher

from config_bot import admins
from message_exept import create_error_message
from loader import mira

async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(admins[0], "Я готова работать, хозяин!")
    except Exception as e:
        mira.telegram_client.post(method="sendMessange", 
                                  params={"text":create_error_message(e), 
                                        "chat_id":admins[0]})
