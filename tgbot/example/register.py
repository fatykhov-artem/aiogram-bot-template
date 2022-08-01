from aiogram import Dispatcher
            
from example.handlers import *


def register_handlers(dp: Dispatcher):
    # Here is the registration of all handlers, example:
    dp.register_message_handler(example_handler)
    pass
