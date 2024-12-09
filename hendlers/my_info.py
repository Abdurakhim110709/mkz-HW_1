from aiogram import Router, types
from aiogram.filters import Command

myinfo = Router()

@myinfo.message(Command('myinfo'))
async def my_info(message: types.Message):
    my_info = (f'ваш id: {message.from_user.id}\n'
               f'ваше имя: {message.from_user.first_name}\n'
               f'ваш username: {message.from_user.username}\n')
    await message.answer(f"ваше info: - {my_info}")