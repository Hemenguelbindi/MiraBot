from aiogram import types, Dispatcher


def register_time_task_handler(dp: Dispatcher):
    pass


async def send_message_time(message: types.Message):
    await message.bot.send_message(222997056, f"Это сообщение отправленно через несколько секунд после старта бота!")


async def send_message_cron(message: types.Message):
    await message.bot.send_message(222997056, f"Это сообщене будет отпровлятся ежедневно в указанное время.")


async def send_message_interval(message: types.Message):
    await message.bot.send_message(222997056, f"Это сообщене будте отправлятся с интервалом в 1 минуту")
    