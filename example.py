import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from asyncio import run
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Hello World!")



async def start():
    await dp.start_polling(bot,polling_timeout=1)


run(start())