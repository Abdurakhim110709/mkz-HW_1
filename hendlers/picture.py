from aiogram import Router, types
from aiogram.filters import Command



picture = Router()



@picture.message(Command("Establishments"))
async def picture_command(message: types.Message):
    photo = types.FSInputFile("images/caffe.jpg")
    await message.answer_photo(
        photo=photo,
        caption="super Establishments"
    )