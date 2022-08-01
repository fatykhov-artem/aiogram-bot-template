from aiogram import Bot

from tgbot.config import config


BotData = Bot(token=config.bot.token, parse_mode=config.bot.parse_mode)