from tgbot.tgbot.aiotelegraph.view import view as view


def text(param):
    return view.text(param)


def set_user_language(param):
    view.user_language.name = param