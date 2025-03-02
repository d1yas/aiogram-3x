import logging
from aiogram import Bot, Dispatcher
from asyncio import run
import asyncio
from config import TOKEN
from app.handlers import router
from app.database.models import async_main

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher()




async def start():
    await async_main()
    dp.include_router(router)
    await dp.start_polling(bot,polling_timeout=1)


# run(start())

if __name__ == '__main__':
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        logging.info("Shutting down")