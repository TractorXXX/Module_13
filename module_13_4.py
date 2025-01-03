from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

import asyncio

api = '***' # Удалил реальный ключ, как было сказано в задании.
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text = 'Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(first = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(second = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(third = message.text)
    data = await state.get_data()

# Упрощённая формула Миффлина - Сан Жеора

    calculator_calories = 10 * int(data['third']) + 6.25 * int(data['second']) - 5 * int(data['first']) + 5
    await message.answer(f'Для похудения или сохранения нормального веса, '
                         f'Вам нужно потреблять не более {calculator_calories} калорий')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)