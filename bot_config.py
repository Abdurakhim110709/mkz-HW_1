from aiogram import Bot, Dispatcher
from dotenv import dotenv_values


token = dotenv_values(".env")["TOKEN_BOT"]
bot = Bot(token=token)
dp = Dispatcher()