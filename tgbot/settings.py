# Bot settings

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

DEFAULT_LANGUAGE = 'en'  # IETF language tag
LIST_LANGUAGES = ['en', 'ru']

PARSE_MODE = 'HTML'

HANDLERS = [
    'tgbot.example'
]

MIDDLEWARES = []

FILTERS = []

EVENTS = []
