from dataclasses import dataclass

from tgbot.aiotelegraph.manage import YalmManager as yalm
from settings import PARSE_MODE


@dataclass
class TgBot:
    token: str
    name: str
    parse_mode: str
    files_chat_id: int


@dataclass
class Config:
    debug: bool
    project_name: str
    url: str
    bot: TgBot


def load_config():
    config_yaml = yalm.load('config.yml')

    return Config(
        debug=config_yaml['debug'],
        project_name=config_yaml['project_name'],
        url=config_yaml['url'],
        bot=TgBot(
            token=config_yaml['bot']['token'],
            name=config_yaml['bot']['name'],
            parse_mode=PARSE_MODE,
            files_chat_id=config_yaml['bot']['files_chat_id']
        )
    )


config = load_config()
