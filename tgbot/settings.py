# Bot settings

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

DEFAULT_LANGUAGE = 'en'  # IETF language tag
LIST_LANGUAGES = ['en', 'ru']

PARSE_MODE = 'HTML'

HANDLERS = [
    'example'
]

MIDDLEWARES = [
    'tgbot.middlewares.set_user_language',
    'tgbot.middlewares.debug_log'
]

FILTERS = []

EVENTS = []
