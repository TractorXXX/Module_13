from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '***' # Удалил реальный ключ, как было сказано в задании
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')

"""До остальных хендлеров из урока программа не дойдет, потому что будет перехвачена предыдущим хендлером.
   Нет нужды в их закомментировании"""

@dp.message_handler(text=['Урбан', 'универ'])
async def urban_message(message):
    print('Urban message!')


@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Start message!')


@dp.message_handler()
async def all_message(message):
    print('Мы получили сообщение!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
