import requests
import json
import os

from aiogram import Bot
from aiogram.types import Message
from dotenv import load_dotenv

from bot.keyboards.register_kb import register_kb
from bot.keyboards.survey_kb import survey_kb

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')


async def get_start(message: Message, bot: Bot):
    url = f"{DATABASE_URL}/bot-users"
    response = requests.get(url=url).text
    data = json.loads(response)
    user_exist = False
    for i in data:
        if i["tg_ID"] == str(message.from_user.id):
            await bot.send_message(message.from_user.id, f'С возвращением, {message.from_user.first_name}! \n'
                                                         f'👇Приступим к опросам?👇', reply_markup=survey_kb)
            user_exist = True
            break
    if user_exist == False:
        await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}! \n'
                                                        f'Этот бот предназначен для прохождения тестов \n'
                                                        f'Для начала необходимо зарегистрироваться\n'
                                                        f'👇Нажмите кнопку зарегистрироваться👇', reply_markup=register_kb)


