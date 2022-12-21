from aiogram import types, Dispatcher

from lexicon import random_hello_user,  help_text, choise_random_gif


def register_privat_user_handlers(dp: Dispatcher)->None:
    dp.register_message_handler(send_command_start_user, commands=['start', 'старт', "Старт"])
    dp.register_message_handler(send_command_help_user, commands=['help', "помощь", "Помощь"])



# Commad Start from user
async def send_command_start_user(message: types.Message):
   await message.bot.send_animation(
                chat_id=message.chat.id,
                animation=choise_random_gif("hello"),                     
                caption=random_hello_user)
   await message.delete()
   

async def send_command_help_user(message: types.Message):
   await message.bot.send_animation(
                chat_id=message.chat.id,
                animation=choise_random_gif("help"),                     
                caption=help_text)
   await message.delete()