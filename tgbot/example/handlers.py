from aiogram import types
import tgbot.example.views as views


async def example_handler(message: types.Message):
    await message.answer('example text')
