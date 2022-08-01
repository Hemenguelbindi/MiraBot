from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config


mira = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

memento = MemoryStorage()

dp = Dispatcher(bot=mira, storage=memento)
