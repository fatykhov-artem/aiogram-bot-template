import os


def create(path_middleware: str, middleware_name: str, middleware_type: str):

    file_data = f"""from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

class {''.join(x.capitalize() for x in middleware_name.split('_'))}(BaseMiddleware):

    async def on_pre_process_update(self, update: types.Update, data: dict):
        pass

    async def on_process_update(self, update: types.Update, data: dict):
        pass
"""

    if middleware_type == 'message':
        file_data += """
    async def on_pre_process_message(self, message: types.Message, data: dict):
        pass

    async def on_process_message(self, message: types.Message, data: dict):
        pass

    async def on_post_process_message(self, message: types.Message, data_from_handler: list, data: dict):
        pass
"""
    elif middleware_type == 'callback':
        file_data += """
    async def on_pre_process_callback_query(self, callback_query: types.CallbackQuery, data: dict):
        pass

    async def on_process_callback_query(self, callback_query: types.CallbackQuery, data: dict):
        pass

    async def on_post_process_callback_query(self, callback_query: types.CallbackQuery, data_from_handler: list, data: dict):
        pass
"""

    file_data += """
    async def on_post_process_update(self, update: types.Update, data_from_handler: list, data: dict):
        pass
"""

    with open(os.path.join(path_middleware), 'w') as f:
        f.write(file_data)