import logging
from xml.etree.ElementInclude import include

from aiogram import Bot, Dispatcher
from asyncio import run
from config import TOKEN
from app.handlers import router

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher()




async def start():
    dp,include(router())
    await dp.start_polling(bot,polling_timeout=1)


run(start())