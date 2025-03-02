import os
import logging
from aiogram import Bot, Dispatcher
from asyncio import run
import asyncio

from dotenv import load_dotenv



logging.basicConfig(level=logging.INFO)

from app.handlers import router
from app.database.models import async_main


async def start():
    await async_main()
    load_dotenv(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot,polling_timeout=1)


# run(start())

if __name__ == '__main__':
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        logging.info("Shutting down")