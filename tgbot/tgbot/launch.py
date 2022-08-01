import os
from pydoc import locate

import yaml
from aiogram import Dispatcher
from loguru import logger as log

from tgbot.tgbot.settings import HANDLERS, MIDDLEWARES


def buttons():
    keyboards_path = 'tgbot/tgbot/keyboards/'
    register_buttons = ['inline', 'reply']

    for register_button in register_buttons:
        open(keyboards_path + f'{register_button}.yml', 'w').close()

    for handler in HANDLERS:
        buttons_path = handler.replace('.', '/')

        for register_button in register_buttons:
            if os.path.exists(buttons_path + f'/buttons/{register_button}.yml'):
                with open(buttons_path + f'/buttons/{register_button}.yml') as line:
                    buttons_yaml = yaml.safe_load(line)

                if buttons_yaml is not None:
                    with open(keyboards_path + f'{register_button}.yml', 'a') as file:
                        yaml.dump(buttons_yaml, file, encoding="utf-8")
    log.success('Buttons running')


def middlewares(dp: Dispatcher):
    for middleware in MIDDLEWARES:
        middleware_class_name = ''.join(x.capitalize() for x in middleware.split('.')[-1].split('_'))
        middleware_class = getattr(locate(middleware), middleware_class_name)
        dp.setup_middleware(middleware_class())
        log.success('Middleware running')


def filters(dp: Dispatcher):
    pass
    log.success('Filters running')


def handlers(dp: Dispatcher):
    for handler in HANDLERS:
        register_handlers = getattr(locate(f'{handler}.register'), 'register_handlers')
        register_handlers(dp)
        log.success('Handlers running')
