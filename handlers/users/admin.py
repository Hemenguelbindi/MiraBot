from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, mira


# Commad Start from admins 
@dp.message_handler(CommandStart(deep_link=None))
async def send_command_start(message: types.Message):
    photo_from_bindi_admin = types.InputFile(path_or_bytesio="photos/admin_me.gif")
    photo_from_kris_admin = types.InputFile(path_or_bytesio="photos/admin_kris.gif")
    match message.chat.id or message.from_user.id:
        
        case 222997056:
            await mira.send_animation(chat_id=message.chat.id,
                                  animation=photo_from_bindi_admin,
                                  caption=("""
                                           Хозяин я умею расказывать про погоду! Вы такой молодец.
                                           Todo для хозяина: Реализовать возможность авто отправки сообщения
                                           """
                                           ))
            
        case 1057974570:
            await mira.send_animation(chat_id=message.chat.id,
                                  animation=photo_from_kris_admin,
                                  caption=(
                                            "Ох, это же самая лучшая хозайка в мире!"
                                            "Так считат ваш муж поцелуйте его!"))
    
