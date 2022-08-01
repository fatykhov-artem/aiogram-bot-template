from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from tgbot.aiotelegraph.view import set_user_language


class SetUserLanguage(BaseMiddleware):

    async def on_pre_process_update(self, update: types.Update, data: dict):
        set_user_language(update.message.from_user.language_code)
