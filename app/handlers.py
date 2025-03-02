from aiogram import types, F, Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,  CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()

class Register(StatesGroup):
    name = State()
    phone = State()

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
    await call.message.edit_text("Callback query", reply_markup= await kb.inline_cars())



@router.message(Command("register"))
async def register_command(message: types.Message,state: FSMContext):
    await state.set_state(Register.name)
    await message.answer("Введите Ваше имя ")

@router.message(Register.name)
async def register_state(message: types.Message,state: FSMContext):
    await state.update_data(name= message.text)
    await state.set_state(Register.phone)
    await message.answer("Введите номер телефона! ")


@router.message(Register.phone)
async def register_phone(message: types.Message,state: FSMContext):
    await state.update_data(phone= message.text)
    data = await state.get_data()
    await message.answer(f"Спасибо за Регистрацию\nName: {data['name']}, Phone: {data['phone']}")
    await state.clear()
