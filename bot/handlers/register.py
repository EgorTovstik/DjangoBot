
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.state.register import RegisterState
from bot.utils.api import create_user
from bot.keyboards.survey_kb import survey_kb


async def start_register(message: Message, state: FSMContext):
    await message.answer(f'Регистрация: \n'
                         f'Укажите как к вам обращаться')
    await state.set_state(RegisterState.regName)


async def register_name(message: Message, state: FSMContext):
    await message.answer(f'Регистрация: \n'
                         f'Укажите Ваш номер телефона \n'
                         f'Телефон записывается в формате 8ХХХХХХХХХХ')
    await state.update_data(regname=message.text)
    await state.set_state(RegisterState.regPhonNum)


async def register_phone_num(message: Message, state: FSMContext):
    await state.update_data(regphone=message.text)
    reg_data = await state.get_data()
    reg_name = reg_data.get('regname')
    reg_phone = reg_data.get('regphone')
    msg = (f'Приятно познакомиться, {reg_name}! \n'
           f'Телефон: {reg_phone}')
    await message.answer(msg)
    create_user(message.from_user.id, reg_name, reg_phone)
    await state.clear()
    await message.answer(f'Регистрация прошла успешно! \n'
                         f'👇Приступим к опросам?👇', reply_markup=survey_kb)

