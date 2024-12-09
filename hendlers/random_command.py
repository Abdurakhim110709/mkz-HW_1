from aiogram import Router, types
from aiogram.filters import Command
import random

random_us = Router()

random_food = [("Кофе - 100"),(" Чай - 50\n"),("Сэндвич - 150\n"),("Суп - 200\n")]


@random_us.message(Command("random_food"))
async def random_command(message: types.Message):
    food = random.choice(random_food)
    await  message.answer(f"Рандомное блюдо: {food}:)")
