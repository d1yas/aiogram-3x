from aiogram import types, F, Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,  CallbackQuery

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Hello World!",reply_markup=kb.main)


@router.message(Command("reply"))
async def reply_command(message: types.Message):
    await message.answer("reply cars",reply_markup= await kb.reply_cars())

@router.message(Command("inline"))
async def inline_cars(message: types.Message):
    await message.answer("Inline cars", reply_markup= await kb.inline_cars())


@router.callback_query(F.data == 'catalog')
async def callback_query_func(call: types.CallbackQuery):
    await call.answer('Вы выбрали каталог', show_alert=True)
    await call.message.edit_text("Callback query", reply_markup=kb.inline_cars())
