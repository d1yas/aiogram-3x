from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup,InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Каталог")
        ],
        [
            KeyboardButton(text="Корзина"),
            KeyboardButton(text="Контакты")
        ]
    ], resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню"
)

settings = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Telegram", url="t.me/djmbv"),
            ]
])


cars = ['Tesla ', 'Mercedes Benz', 'BMW',]

async def reply_cars():
    keyboard = ReplyKeyboardBuilder()
    for car in cars:
        keyboard.add(KeyboardButton(text=car))
    return keyboard.adjust(2).as_markup()

cars_2 = ['Ferrari', 'RR', 'Bentli',]

async def inline_cars():
    keyboard_2 = InlineKeyboardBuilder()
    for car in cars_2:
        keyboard_2.add(InlineKeyboardButton(text=car,url="t.me/djmbv"))
    return keyboard_2.adjust(2).as_markup()
