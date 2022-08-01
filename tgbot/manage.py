import os
from sys import argv

from tgbot.aiotelegraph.manage import middleware, handler

help_text = f"""Help commands:

create handler <file_name>
create middleware <file_name> <middleware_type>
create event <file_name>
create filter <file_name>
"""

match argv[1:]:
    case ['create', 'middleware', file_name, middleware_type]:
        path = os.path.join('./tgbot/middlewares/', file_name + '.py')
        middleware.create(path, file_name, middleware_type)
        print(f'{file_name} middleware is created')

    case ['create', 'handler', file_name]:
        path = os.path.join('./', file_name)
        handler.create(path, file_name)
        print(f'{file_name} handler is created')

    case ['help']:
        print(help_text)
    case _:
        print(f'Not found command. {help_text}')
