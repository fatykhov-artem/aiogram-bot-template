import os
import shutil
from pydoc import locate

from aiogram import Dispatcher
from loguru import logger as log
import yaml

from settings import HANDLERS, MIDDLEWARES, LIST_LANGUAGES, DEFAULT_LANGUAGE, ROOT_DIR
from tgbot.aiotelegraph.manage import TextManager


def buttons():
    keyboards_path = 'tgbot/keyboards'
    register_buttons = ['inline', 'reply']

    for root, dirs, files in os.walk(f'{keyboards_path}'):
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))

    for handler in HANDLERS:
        buttons_path = handler.replace('.', '/')

        for register_button in register_buttons:
            register_button_name = f'{register_button}.yml'
            buttons_yaml_path = f'{buttons_path}/buttons/{register_button_name}'
            if os.path.exists(buttons_yaml_path):
                buttons_yaml = TextManager.load(buttons_yaml_path)

                if buttons_yaml is not None:
                    for language in LIST_LANGUAGES:
                        os.mkdir(f'{ROOT_DIR}/{keyboards_path}/{language}')

                        button_data_path = f'{ROOT_DIR}/{keyboards_path}/{language}/{register_button_name}'
                        if not os.path.exists(button_data_path):
                            open(button_data_path, 'w').close()

                        buttons_texts_path = f'{buttons_path}/texts'
                        buttons_texts = TextManager.load(f'{buttons_texts_path}/{language}/{register_button_name}')
                        default_buttons_texts = TextManager.load(
                            f'{buttons_texts_path}/{DEFAULT_LANGUAGE}/{register_button_name}'
                        )

                        for button_name in buttons_yaml:
                            text = None
                            if buttons_texts is not None and button_name in buttons_texts:
                                text = buttons_texts[button_name]
                            else:
                                if default_buttons_texts is not None and button_name in default_buttons_texts:
                                    log.warning(
                                        f'Not found button localization. Button: {button_name}. Language: {language}'
                                    )
                                    text = default_buttons_texts[button_name]
                                else:
                                    log.error(f'Not found button text. Button: {button_name}. Language: {language}')
                                    break

                            if text is not None:
                                with open(button_data_path, 'a') as file:
                                    yaml.dump({
                                        button_name: {
                                            'text': text,
                                            'callback_data': buttons_yaml[button_name]
                                        }
                                    }, file, encoding="utf-8")
            else:
                log.error(f'Not found {register_button} buttons. Handler: {handler}')

    log.success('Buttons created')


def middlewares(dp: Dispatcher):
    for middleware in MIDDLEWARES:
        middleware_class_name = ''.join(x.capitalize() for x in middleware.split('.')[-1].split('_'))
        middleware_class = getattr(locate(middleware), middleware_class_name)
        dp.setup_middleware(middleware_class())
    log.success('Middlewares running')


def filters(dp: Dispatcher):
    log.success('Filters running')


def handlers(dp: Dispatcher):
    for handler in HANDLERS:
        register_handlers = getattr(locate(f'{handler}.register'), 'register_handlers')
        register_handlers(dp)
    log.success('Handlers running')
