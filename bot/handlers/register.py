
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.state.register import RegisterState
from bot.utils.api import create_user
from bot.keyboards.survey_kb import survey_kb, quest_kb


# Ожидание имени пользователя
async def start_register(message: Message, state: FSMContext):
    await message.answer(f'Регистрация: \n'
                         f'Укажите как к вам обращаться')
    await state.set_state(RegisterState.regName)


# Сохранение имени пользователя и ожидание номера телефона
async def register_name(message: Message, state: FSMContext):
    await message.answer(f'Регистрация: \n'
                         f'Укажите Ваш номер телефона \n'
                         f'Телефон записывается в формате 8ХХХХХХХХХХ')
    await state.update_data(regname=message.text)
    await state.set_state(RegisterState.regPhonNum)


# Сохранение номера телефона и ожидание согласия на рассылку
async def register_phone_num(message: Message, state: FSMContext):
    await message.answer(f'Регистрация окончена, хотели бы вы получать рассылку о наших новых опросах?',
                         reply_markup=quest_kb)
    await state.update_data(regphone=message.text)
    await state.set_state(RegisterState.consentMailList)


# Сохранение согласия на рассылку и передача полученных данных в базу данных
async def register_consent(message: Message, state: FSMContext):
    await state.update_data(regconsent=message.text)
    reg_data = await state.get_data()
    reg_name = reg_data.get('regname')
    reg_phone = reg_data.get('regphone')
    reg_consent = reg_data.get('regconsent')
    msg = (f'Приятно познакомиться, {reg_name}! \n'
           f'Телефон: {reg_phone}')
    await message.answer(msg)
    create_user(message.from_user.id, reg_name, reg_phone, reg_consent)
    await state.clear() # Очистка данных из машины состояний "Пользователи"
    await message.answer(f'Регистрация прошла успешно! \n'
                         f'👇Приступим к опросам?👇', reply_markup=survey_kb)

