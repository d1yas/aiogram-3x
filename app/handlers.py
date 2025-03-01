from aiogram import types, F, Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Hello World!")

