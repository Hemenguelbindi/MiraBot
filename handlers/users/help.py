from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp, mira

# Commad help
@dp.message_handler(CommandHelp())
async def send_help(message: types.Message):
    helps_anime = types.InputFile(path_or_bytesio="photos/command_help/Help.gif")
    docs_helps = (
            "Mira\n"
            "Version 0.1.8\n"
            "Описание комманд:\n"
            "/weather - позволяет узнать погоду, при использование нужно указать название города\n"
            "Работает как с латиницей так и с кирилицей\n"
            "(Moscow, Saratov, Ufa and ect)"
    )
    await mira.send_animation(
        chat_id=message.chat.id,
        animation=helps_anime,
        caption=docs_helps,
    )
