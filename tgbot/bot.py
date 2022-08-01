import asyncio

from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger as log

from tgbot import aiotelegraph
from tgbot.config import config
import tgbot.launch as launch


async def main():
    if not config.debug:
        log.remove()

    storage = MemoryStorage()
    dp = Dispatcher(aiotelegraph.bot, storage=storage)

    launch.buttons()
    launch.middlewares(dp)
    launch.filters(dp)
    launch.handlers(dp)

    try:
        log.success('Bot started')
        await dp.start_polling()
    finally:
        log.error('Bot stopped')
        await dp.storage.close()
        await dp.storage.wait_closed()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        log.error('Bot stopped')
