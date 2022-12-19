import asyncio
from loguru import logger

from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config


logger.add("logs/file_{time}.log", format="{time} {level} {message}", rotation="1 week", compression="zip")

# Фнукция для регистрации всех хэндлеров
def register_all_handlers(dp: Dispatcher) -> None:
    pass


# Функция конфигурирования и запуска бота
async def main():
        
    logger.info("Start bot")
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(bot)

    # Настраиваем главное меню бота
    # await set_main_menu(dp)

    # Регистрируем все хэндлеры
    register_all_handlers(dp)

    # Запускаем polling
    try:
        await dp.start_polling()
    finally:
        await bot.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped!')