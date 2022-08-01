import os
from dataclasses import dataclass

import yaml

from settings import DEFAULT_LANGUAGE


@dataclass
class UserLanguage:
    name: str


user_language = UserLanguage(name=DEFAULT_LANGUAGE)


def text(file_name: str, file_type: str, file_path: str):
    path = file_path + 'texts'

    if not os.path.exists(f'{path}{file_name}.{file_type}'):
        file_path = f'{path}/{user_language.name}/{file_name}.{file_type}'
    else:
        file_path = f'{path}/{DEFAULT_LANGUAGE}/{file_name}.{file_type}'

    match file_type:
        case 'yml':
            with open(file_path) as line:
                file = yaml.safe_load(line)

    return file

