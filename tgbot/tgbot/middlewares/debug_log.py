from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from loguru import logger as log


class DebugLog(BaseMiddleware):

    async def on_pre_process_update(self, update: types.Update, data: dict):
        log.debug(update)

    async def on_post_process_update(self, update: types.Update, data_handler: list, data: dict):
        log.success('Message been sent')
