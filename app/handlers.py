from aiogram import types, F, Router
from aiogram.filters import CommandStart,Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import app.database.request as rq


import app.keyboards as kb
# from app.middlewares import TestMiddleware

router = Router()

# router.message.outer_middleware(TestMiddleware())

class Register(StatesGroup):
    name = State()
    phone = State()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await rq.set_users(message.from_user.id)
    await message.answer("Добро пожаловать в магазин кросовок",reply_markup=kb.main)




