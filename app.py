import asyncio
from loguru import logger

from aiogram import Bot, Dispatcher
from keyboards.set_menu import set_main_menu
from handlers.admin_handlers import register_admin_handler
from config_data.config import Config, load_config


logger.add("logs/{time}.log", format="{time} {level} {message}", rotation="1 week", compression="zip")
config: Config = load_config()




# Фнукция для регистрации всех хэндлеров
def register_all_handlers(dp: Dispatcher) -> None:
    register_admin_handler(dp)


# Функция конфигурирования и запуска бота
async def main():
        
    logger.info("Start bot")
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    mira_bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(mira_bot)
    # Настраиваем главное меню бота
    await set_main_menu(dp)

    # Регистрируем все хэндлеры
    register_all_handlers(dp)

    # Запускаем polling
    try:
        await dp.start_polling()
    finally:
        await mira_bot.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped!')