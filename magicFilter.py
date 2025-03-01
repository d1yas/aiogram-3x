import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart,Command
from aiogram.types import Message, ContentType
from asyncio import run
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Hello World!")


@dp.message(F.text == "Python")
async def cmd_text(message: Message):
    await message.answer("Python bu dasturlash tili! ")

@dp.message(F.text.startswith("Salom"))
async def cmd_startwidth(message: Message):
    await message.answer(f"Assalomu Aleykum: {message.from_user.first_name}")

@dp.message(F.content_type == types.ContentType.PHOTO)
async def photo_handler(message: Message):
    await message.answer_photo(message.photo[-1].file_id)

@dp.message(F.text.len() > 5)
async def cmd_len(message: Message):
    await message.answer("Len")

@dp.message(F.from_user.id == 6812498519)
async def cmd_user(message: Message):
    await message.answer("Check user ID")

@dp.message(F.text.startswith("Salom") & F.text.len() > 5)
async def and_filter(message: Message):
    await message.answer("CHECK and LOOP ")

@dp.message(F.text.startswith("Hello") | F.text.endswith("Hi"))
async def cmd_or(message: Message):
    await message.answer("CHECL or LOOP")

@dp.message(F.text.not_().startswith("/") | F.text.endswith("start"))
async def cmd_not(message: Message):
    await message.answer("not check")

async def start():
    await dp.start_polling(bot,polling_timeout=1)








run(start())
