from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from tk_client import TelegramClient

from config_bot import BOT_TOKEN, admins, CONNECT_LINK

class MiraBot(Bot):
    def __init__(self, telegram_client: TelegramClient, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.telegram_client = telegram_client
        
miraclient = TelegramClient(token=BOT_TOKEN, base_url=CONNECT_LINK)
mira = MiraBot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML, telegram_client=miraclient)

memento = MemoryStorage()

dp = Dispatcher(bot=mira, storage=memento)
