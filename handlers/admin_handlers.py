from aiogram import types, Dispatcher
from config_data.config import get_admins
from lexicon import choise_random_gif, ANSWER_ADMIN


def register_admin_handler(dp: Dispatcher):
    dp.register_message_handler(send_command_start_admin, commands=['start'])


# Commad Start from admins 
async def send_command_start_admin(message: types.Message):
    admins = get_admins()
    for admin in admins:
        if admin == admins[0]:
            await message.bot.send_animation(
                chat_id=admin,
                animation=choise_random_gif("hello"),
                caption=ANSWER_ADMIN["Victor"])
            await message.delete()
        # если по другому тогда отправить другому админу
        if admin == admins[1]:
            await message.bot.send_animation(chat_id=admin,
                                         animation=choise_random_gif("hello"),
                                         caption=ANSWER_ADMIN["Kristina"])
            await message.delete()
