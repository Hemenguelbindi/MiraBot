from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, mira
from configurations import config


@dp.message_handler(CommandStart(deep_link=None))
async def bot_start_from_admin(message: types.Message):
    photo_from_all = types.InputFile(path_or_bytesio="photos/anime_girl.gif")
    photo_from_bindi_admin = types.InputFile(path_or_bytesio="photos/admin_me.gif")
    photo_from_kris_admin = types.InputFile(path_or_bytesio="photos/admin_kris.gif")
    if message.chat.id == config.admins[0]:
        await mira.send_animation(chat_id=message.chat.id,
                                  animation=photo_from_bindi_admin,
                                  caption="Хозяин вы меня допишите пожалуйста! А то я ничего не умею.")
    elif message.chat.id == config.admins[1]:
        await mira.send_animation(chat_id=message.chat.id, animation=photo_from_kris_admin, caption="Ох, это же самая лучгкая хозайка в мире, так считат ваш муж поцелуйте его!")
    elif message.chat.id not in config.admins:
        await mira.send_animation(chat_id=message.chat.id,
                              animation=photo_from_all,
                              caption=f"""Привет, {message.from_user.full_name}! Хорошего вам дня! """)
