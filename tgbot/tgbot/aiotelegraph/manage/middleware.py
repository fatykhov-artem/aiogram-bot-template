import os


def create(path_middleware: str, middleware_name: str, middleware_types: list):
    file_data = f"""from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware


class {''.join(x.capitalize() for x in middleware_name.split('_'))}(BaseMiddleware):

    async def on_pre_process_update(self, update: types.Update, data: dict):
        pass

    async def on_process_update(self, update: types.Update, data: dict):
        pass
"""

    group_middleware_types = {
        'message': """
    async def on_pre_process_message(self, message: types.Message, data: dict):
        pass

    async def on_process_message(self, message: types.Message, data: dict):
        pass

    async def on_post_process_message(self, message: types.Message, data_from_handler: list, data: dict):
        pass
""",
        'callback_answer': """
    async def on_pre_process_callback_query(self, callback_query: types.CallbackQuery, data: dict):
        pass

    async def on_process_callback_query(self, callback_query: types.CallbackQuery, data: dict):
        pass

    async def on_post_process_callback_query(self, callback_query: types.CallbackQuery, data_from_handler: list, data: dict):
        pass
"""
    }

    for middleware_type in middleware_types:
        key = middleware_type[1:]
        if key in group_middleware_types:
            file_data += group_middleware_types[middleware_type[1:]]

    file_data += """
    async def on_post_process_update(self, update: types.Update, data_from_handler: list, data: dict):
        pass
"""

    with open(os.path.join(path_middleware), 'w') as f:
        f.write(file_data)
