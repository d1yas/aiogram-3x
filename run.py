import os
import logging
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Загрузка переменных окружения
load_dotenv()

# Получаем токен из .env
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("Переменная окружения TOKEN не установлена!")

# Создаем экземпляр бота
bot = Bot(token=TOKEN)

# Импортируем маршрутизатор и базу данных
from app.handlers import router
from app.database.models import async_main

async def start():
    await async_main()  # Подключение к БД
    dp = Dispatcher()
    dp.include_router(router)  # Подключаем обработчики
    await dp.start_polling(bot, polling_timeout=1)

if __name__ == '__main__':
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        logging.info("Shutting down")
