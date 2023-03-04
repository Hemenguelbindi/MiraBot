from aiogram import types, Dispatcher

from lexicon.lexicon_ru import MessageSelector, ImagesSelector


def register_admin_handler(dp: Dispatcher):
    dp.register_message_handler(send_command_start_admin, commands=['start'])


# Commad Start from admins 
async def send_command_start_admin(message: types.Message):
    msg_admin = MessageSelector()
    img = ImagesSelector()
    match message.chat.id or message.from_user.id:
        case 222997056:
            await message.bot.send_animation(
                chat_id=message.chat.id,
                animation=img.random_img("hello"),
                caption=msg_admin.message_admin("Victor")
            )
            await message.delete()

        case 1057974570:
            await message.bot.send_animation(
                chat_id=message.chat.id,
                animation=img.random_img("hello"),
                caption=msg_admin.message_admin("Kristina")
            )
            await message.delete()
