

from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.state.survey import SurveyState
from bot.utils.api import create_survey
from bot.keyboards.survey_kb import quest_kb


async def start_survey(message: Message, state: FSMContext):
    await message.answer(f'Первый вопрос {message.from_user.first_name} \n'
                         f'...', reply_markup=quest_kb)
    await state.set_state(SurveyState.quest1)


async def survey_quest1(message: Message, state: FSMContext):
    await message.answer(f'Второй вопрос \n'
                         f'...', reply_markup=quest_kb)
    await state.update_data(surquest1=message.text)
    await state.set_state(SurveyState.quest2)


async def survey_quest2(message: Message, state: FSMContext):
    await message.answer(f'Третий вопрос \n'
                         f'...', reply_markup=quest_kb)
    await state.update_data(surquest2=message.text)
    await state.set_state(SurveyState.quest3)


async def survey_quest3(message: Message, state: FSMContext):
    await message.answer(f'Четвертый вопрос \n'
                         f'...', reply_markup=quest_kb)
    await state.update_data(surquest3=message.text)
    await state.set_state(SurveyState.quest4)


async def survey_quest4(message: Message, state: FSMContext):
    await state.update_data(surquest4=message.text)
    surv_data = await state.get_data()
    surv_quest1 = surv_data.get('surquest1')
    surv_quest2 = surv_data.get('surquest2')
    surv_quest3 = surv_data.get('surquest3')
    surv_quest4 = surv_data.get('surquest4')
    await message.answer('Поздравляю! Вы прошли все вопросы,\n'
                         'результаты вы можете посмотреть на нашем сайте')
    msg = (f'Ваши ответы на вопросы:\n'
           f'{surv_quest1} \n'
           f'{surv_quest2} \n'
           f'{surv_quest3} \n'
           f'{surv_quest4} \n')
    await message.answer(msg)
    create_survey(message.from_user.id, surv_quest1, surv_quest2, surv_quest3, surv_quest4)
    await state.clear()

