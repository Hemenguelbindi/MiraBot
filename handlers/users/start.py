from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, mira



# Commad Start
@dp.message_handler(CommandStart(deep_link=None))
async def send_command_start(message: types.Message):
    photo_from_all = types.InputFile(path_or_bytesio="photos/anime_girl.gif")
    await mira.send_animation(chat_id=message.chat.id,animation=photo_from_all,
                                  caption=f"""Привет, {message.from_user.full_name}! Хорошего вам дня!"""
                             )
