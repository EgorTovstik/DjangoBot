

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)


survey_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Перейти к опросам')
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Нажмите кнопку')


quest_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Да")],
    [KeyboardButton(text="Нет")],
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Нажмите кнопку')

