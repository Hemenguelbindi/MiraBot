from aiogram.dispatcher.filters.state import StatesGroup, State


class DateWeather(StatesGroup):
    City = State()
