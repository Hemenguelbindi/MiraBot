from utils.set_bot_commands import set_default_commands
from utils.notify_admins import on_startup_notify
from message_exept import create_error_message
from config_bot import admins


async def on_startup(dp):
    await on_startup_notify(dp)
    await set_default_commands(dp)



if __name__ == "__main__":
    
    from aiogram import executor
    from handlers import dp
    from tk_client import TelegramClient
    try:
        executor.start_polling(dp, on_startup=on_startup)
    except Exception as e:
        telegram_client = TelegramClient()
        telegram_client.post(method="sendMessange", 
                                  params={"text":create_error_message(e), 
                                            "chat_id":admins})
