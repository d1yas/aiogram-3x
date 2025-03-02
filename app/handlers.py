from aiogram import types, F, Router
from aiogram.filters import CommandStart,Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import app.database.request as rq


import app.keyboards as kb
# from app.middlewares import TestMiddleware

router = Router()

# router.message.outer_middleware(TestMiddleware())

class Register(StatesGroup):
    name = State()
    phone = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_users(message.from_user.id)
    await message.answer("Добро пожаловать в магазин кросовок",reply_markup=kb.main)

@router.message(F.text == "Каталог")
async def catalog(message: Message):
    await message.answer('Выберите категорию товара',reply_markup=await kb.categories())

@router.callback_query(F.data.startswith('category_'))
async def category(call: CallbackQuery):
    await call.answer("Вы выбрали категорию")
    await call.message.answer("Выберите товар по категории", reply_markup= await kb.items(call.data.split('_')[1]))


@router.callback_query(F.data.startswith('item_'))
async def category(call: CallbackQuery):
    await call.answer("Вы выбрали товар")

    item_data = await rq.get_item_category(call.data.split('_')[1])

    if item_data:
        await call.message.answer(
            f"Название: {item_data.name}\n"
            f"Описание: {item_data.description}\n"
            f"Цена: {item_data.price} $",
            reply_markup=await kb.items(call.data.split('_')[1])
        )
    else:
        await call.message.answer("Товар не найден.")
