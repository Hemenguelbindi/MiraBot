from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp, mira



@dp.message_handler(CommandHelp())
async def send_help(message: types.Message):
    await mira.send_animation(

        text=(
            "Mira\n"
            "Version 0.1.1\n"
            "Описание комманд:"
            """
            /weather - позволяет узнать погоду,
            при использоание нужно указать город
            в соотвествее с примером на латинице
            (Moscow, Saratov, Ufa and ect)
            """
        )
    )
