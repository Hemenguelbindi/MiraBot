from utils.set_bot_commands import set_default_commands
from utils.notify_admins import on_startup_notify
from message_exept import create_error_message



async def on_startup(dp):
    await on_startup_notify(dp)
    await set_default_commands(dp)



if __name__ == "__main__":
    
    from aiogram import executor
    from config_bot import admin_hemen
    from loader import mira
    from handlers import dp
    
    try:
        executor.start_polling(dp, on_startup=on_startup)
    except (KeyboardInterrupt, SystemExit) as k:
        mira.telegram_client.post(method="sendMessange", 
                                  params={"text":create_error_message(k), 
                                            "chat_id":admin_hemen})    
    except Exception as e:
        mira.telegram_client.post(method="sendMessange", 
                                  params={"text":create_error_message(e), 
                                            "chat_id":admin_hemen})
