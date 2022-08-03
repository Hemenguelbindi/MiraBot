from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, mira
from configurations import config


@dp.message_handler(CommandStart(deep_link=None))
async def send_command_start(message: types.Message):
    photo_from_all = types.InputFile(path_or_bytesio="photos/anime_girl.gif")
    photo_from_bindi_admin = types.InputFile(path_or_bytesio="photos/admin_me.gif")
    photo_from_kris_admin = types.InputFile(path_or_bytesio="photos/admin_kris.gif")

    if message.chat.id == config.admins[0] or message.from_user.id == config.admins[0]:
        await mira.send_animation(chat_id=message.chat.id,
                                  animation=photo_from_bindi_admin,
                                  caption=("""
                                           Хозяин я умею расказывать про погоду! Вы такой молодец.
                                           Todo для хозяина: хозаин проблема с коммандой weather
                                           она постоянно падает с ошибкой:
                                           "Message.answer_animation() got an unexpected keyword argument 'chat_id'"
                                           """
                                           ))

    elif message.chat.id == config.admins[1] or message.from_user.id == config.admins[0]:
        await mira.send_animation(chat_id=message.chat.id,
                                  animation=photo_from_kris_admin,
                                  caption=(
                                            "Ох, это же самая лучшая хозайка в мире!"
                                            "Так считат ваш муж поцелуйте его!")
                                  )

    elif message.chat.id not in config.admins or message.from_user.id not in config.admins:
        await mira.send_animation(chat_id=message.chat.id,
                                  animation=photo_from_all,
                                  caption=f"""Привет, {message.from_user.full_name}! Хорошего вам дня! """
                                  )
