from aiogram import types, Dispatcher

from lexicon import random_hello_user, get_random_hello, get_random_help, help_text


def register_user_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(send_command_start_user, commands=['start', 'старт', "Старт"])
    dp.register_message_handler(send_command_help_user, commands=['help', "помощь", "Помощь"])



# Commad Start from user
async def send_command_start_user(message: types.Message):
   await message.bot.send_animation(
                chat_id=message.chat.id,
                animation=get_random_hello(),                     
                caption=random_hello_user)
   await message.delete()
   

async def send_command_help_user(message: types.Message):
   await message.bot.send_animation(
                chat_id=message.chat.id,
                animation=get_random_help(),                     
                caption=help_text)
   await message.delete()