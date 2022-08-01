import inspect

from tgbot.aiotelegraph.view import view as view


def text(file_name: str, file_type: str = 'yml'):
    file_path = inspect.stack()[1].filename.replace('views.py', '')
    return view.text(file_name, file_type, file_path)


def set_user_language(language_name: str):
    view.user_language.name = language_name