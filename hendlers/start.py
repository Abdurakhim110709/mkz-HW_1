from aiogram import Router, types
from aiogram.filters import Command
start_router = Router()
@start_router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот кафе. Чем могу помочь?"
                         """
                         наше заведения:/Establishments
                         Наше меню:/menu
                         Время работы:/hours
                         : /random_food
                         """)



