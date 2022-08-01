from aiogram import Dispatcher
            
from tgbot.example.handlers import *


def register_handlers(dp: Dispatcher):
    # Here is the registration of all handlers, example:
    dp.register_message_handler(example_handler)
    pass
