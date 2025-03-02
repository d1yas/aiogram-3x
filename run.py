import logging

from aiogram import Bot, Dispatcher
from asyncio import run
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher()




async def start():
    dp.include_router(router)
    await dp.start_polling(bot,polling_timeout=1)


run(start())