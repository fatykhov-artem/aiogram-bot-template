import os

from settings import LIST_LANGUAGES


def create(path_handler: str, handler_name: str):
    path_handler_array = path_handler.split('/')
    for i in range(4, len(path_handler_array ) +1):
        add_path = '/'.join(path_handler_array[:i])
        if not os.path.exists(add_path):
            os.mkdir(add_path)

    open(os.path.join(path_handler, '__init__.py'), 'w')

    with open(os.path.join(path_handler, 'handlers.py'), 'w') as f:
        f.write(
            f"""from aiogram import types
import tgbot.handlers.{handler_name}.views as views


async def {handler_name}_handler(message: types.Message):
    await message.answer('example {handler_name}')
"""
        )

    with open(os.path.join(path_handler, 'register.py'), 'w') as f:
        f.write(
            f"""from aiogram import Dispatcher

from tgbot.handlers.{handler_name}.handlers import *


def register_handlers(dp: Dispatcher):
    # Here is the registration of all handlers, example:
    # dp.register_message_handler({handler_name}_handler)
    pass
"""
        )

        with open(os.path.join(path_handler, 'views.py'), 'w') as f:
            f.write(
                f"""from jinja2 import Template
import tgbot.tgbot.aiograph.view as view


def massage_view(data):
    messages_text = view.text('{handler_name}.yml')

    text = 'text'
    markup = []

    # code

    return text, markup
    """
            )

    os.mkdir(os.path.join(path_handler, 'buttons'))
    with open(os.path.join(path_handler, 'buttons/inline.yml'), 'w') as f:
        f.write(f'# Inline buttons: {handler_name}\n\n')

    with open(os.path.join(path_handler, 'buttons/reply.yml'), 'w') as f:
        f.write(f'# Reply buttons: {handler_name}\n\n')

    for language_name in LIST_LANGUAGES:
        os.mkdir(os.path.join(path_handler, f'texts/{language_name}'))
        with open(os.path.join(path_handler, f'texts/{language_name}/{handler_name}.yml'), 'w') as f:
            f.write(f'# Texts message: {handler_name}\n\n')
        with open(os.path.join(path_handler, f'texts/{language_name}/inline.yml'), 'w') as f:
            f.write(f'# Texts inline buttons: {handler_name}\n\n')
        with open(os.path.join(path_handler, f'texts/{language_name}/reply.yml'), 'w') as f:
            f.write(f'# Texts reply buttons: {handler_name}\n\n')

    os.mkdir(os.path.join(path_handler, 'scrips'))
    open(os.path.join(f'{path_handler}/scrips', '__init__.py'), 'w')

    os.mkdir(os.path.join(path_handler, 'media'))