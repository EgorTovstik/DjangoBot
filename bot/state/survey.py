

from aiogram.fsm.state import StatesGroup, State


class SurveyState(StatesGroup):
    quest1 = State()
    quest2 = State()
    quest3 = State()
    quest4 = State()
