import asyncio
from datetime import datetime

from loguru import logger

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards.set_menu import set_main_menu
from handlers import register_admin_handler, register_privet_user_handlers, register_user_handlers
from handlers_tasks import send_weather, send_active_care
from config_data import Config, load_config

logger.add("logs/{time}.log", format="{time} {level} {message}", rotation="1 week", compression="zip")

config: Config = load_config()


# Фнукция для регистрации всех хэндлеров
def register_all_handlers(dp: Dispatcher) -> None:
    register_admin_handler(dp)
    register_privet_user_handlers(dp)
    register_user_handlers(dp)


# Функция конфигурирования и запуска бота
async def main():
    logger.info("Start bot")
    logger.info("Get configuration")
    setting: Config = load_config()
    logger.info("Init memory")
    storage: MemoryStorage = MemoryStorage()
    # Инициализируем бот и диспетчер
    mira_bot: Bot = Bot(token=setting.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(mira_bot, storage=storage)
    scheduler = AsyncIOScheduler(timezone="Asia/Yekaterinburg")
    scheduler.add_job(send_weather, trigger='cron', hour='9', minute='50',
                      start_date=datetime.now(),
                      kwargs={'bot': mira_bot})
    scheduler.add_job(send_active_care, trigger='cron', hour="9", minute='50',
                      start_date=datetime.now(),
                      kwargs={'bot': mira_bot})
    scheduler.start()
    # Настраиваем главное меню бота
    await set_main_menu(dp)

    # Регистрируем все хэндлеры
    register_all_handlers(dp)

    # Запускаем polling
    try:
        logger.info("Start polling")
        await dp.start_polling()
    finally:
        await mira_bot.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped!')
