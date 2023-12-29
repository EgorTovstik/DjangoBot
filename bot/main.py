
import asyncio
import os
import logging
import sys

from dotenv import load_dotenv
from aiogram import Dispatcher, Bot, F
from aiogram.enums import ParseMode
from aiogram.filters import Command

from utils.commands import set_commands
from state.register import RegisterState
from state.survey import SurveyState
from handlers.start import get_start
from handlers.register import (start_register, register_name, register_phone_num, register_consent)
from handlers.survey import (start_survey, survey_quest1, survey_quest2,
                             survey_quest3, survey_quest4)


load_dotenv()

token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')

dp = Dispatcher()
bot = Bot(token, parse_mode=ParseMode.HTML)


async def start_bot(bot: Bot):
    await bot.send_message(admin_id, text='Бот запущен')

# команда старт
dp.startup.register(start_bot)
dp.message.register(get_start, Command(commands='start'))


# хендлер регистрации
dp.message.register(start_register, F.text == 'Зарегистрироваться')
dp.message.register(register_name, RegisterState.regName)
dp.message.register(register_phone_num, RegisterState.regPhonNum)
dp.message.register(register_consent, RegisterState.consentMailList)

# хендлер прохождения опроса
dp.message.register(start_survey, F.text == 'Перейти к опросам')
dp.message.register(survey_quest1, SurveyState.quest1)
dp.message.register(survey_quest2, SurveyState.quest2)
dp.message.register(survey_quest3, SurveyState.quest3)
dp.message.register(survey_quest4, SurveyState.quest4)


async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start())

