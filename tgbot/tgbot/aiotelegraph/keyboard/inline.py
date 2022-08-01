import yaml
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.misc.helper import yalm_load

inline_buttons = yalm_load('tgbot/keyboards/buttons/inline.yml')


def get_inline_markup(
        button_names: list,
        row_width: int = 1, error_id: str = None, url_data: tuple = ()) -> InlineKeyboardMarkup:
    """
    Генерирует и возвращает markup в зависимости от именно кнопки
    :param error_id:
    :param button_names:
    :param row_width:
    :param url_data:
    :return markup:
    """

    markup = InlineKeyboardMarkup(row_width=row_width)
    for button_name in button_names:
        if button_name in inline_buttons:
            button = inline_buttons[button_name]
            callback_data = None
            if 'url' not in button['callback_data']:
                callback_data = callback_data_class().new(
                    id=error_id,
                    action=button['callback_data']['action'] if 'action' in button['callback_data'] else '',
                    view=button['callback_data']['view'] if 'view' in button['callback_data'] else ''
                )

            markup.insert(
                InlineKeyboardButton(
                    text=button['text'],
                    url=button['callback_data']['url'].format(*url_data) if 'url' in button['callback_data'] else None,
                    callback_data=callback_data
                )
            )

    return markup


def get_inline_back_page(format_data: tuple = ()) -> InlineKeyboardMarkup:
    """
    Возвращает markup для кнопки назад
    :param format_data:
    :return markup:
    """

    markup = InlineKeyboardMarkup(row_width=1)
    button = inline_buttons['back_page']
    markup.insert(
        InlineKeyboardButton(
            text=button['callback_query_text'],
            callback_data=button['callback_data'].format(*format_data)
        )
    )
    return markup
