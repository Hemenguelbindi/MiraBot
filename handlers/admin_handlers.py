from aiogram import types, Dispatcher

from lexicon import choise_random_gif, ANSWER_ADMIN


def register_admin_handler(dp: Dispatcher):
    dp.register_message_handler(send_command_start_admin, commands=['start'])


# Commad Start from admins 
async def send_command_start_admin(message: types.Message):
    match message.chat.id or message.from_user.id:
        case 222997056:
            await message.bot.send_animation(
                chat_id=message.chat.id,
                animation=choise_random_gif("hello"),                     
                caption=ANSWER_ADMIN["Victor"])
        case 1057974570:
            await message.bot.send_animation(chat_id=message.chat.id,
                animation=choise_random_gif("hello"),
                caption=ANSWER_ADMIN["Kristina"])