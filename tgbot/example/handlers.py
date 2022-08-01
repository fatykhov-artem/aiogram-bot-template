from aiogram import types
import example.views as views


async def example_handler(message: types.Message):
    text, markup = views.example_view()
    await message.answer(text)
