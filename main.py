import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values
import random

token = dotenv_values(".env")["TOKEN_bot"]
bot = Bot(token=token)
dp = Dispatcher()

users = ['Maga','Raha','Baha','Ilya','Boris','Rakhim','Makaza']
@dp.message(Command("random"))
async def random_command(message: types.Message):
    person = random.choice(users)
    await  message.answer(f"Рандомное имя:  {person}")



@dp.message(Command('myinfo'))
async def my_info(message: types.Message):
    my_info = (f'ваш id: {message.from_user.id}\n'
               f'ваше имя: {message.from_user.first_name}\n'
               f'ваш username: {message.from_user.username}\n')
    await message.answer(f"ваше info: - {my_info}")

@dp.message(Command('start'))
async def start(message : types.Message):
    name = message.from_user.first_name

    c1 = "/start"
    c2 = "/myinfo"
    c3 = "/random"
    await message.answer(f"привет - {name}\n"
                          f"мои команды:\n"
                         f"{c1}\n"
                         f"{c2}\n"
                         f"{c3}\n")
                        
async def main():
    #Запуск бота
    await dp.start_polling(bot)



if __name__ == '__main__':
   asyncio.run(main())
