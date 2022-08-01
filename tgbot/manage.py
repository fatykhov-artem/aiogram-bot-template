import os
from sys import argv

from tgbot.aiotelegraph.manage import middleware, handler

help_text = f"""Help commands:

create handler <file_name>
create middleware <file_name> <middleware_types>
create event <file_name>
create filter <file_name>
"""

match argv[1:]:
    case ['create', 'middleware', file_name, *middleware_types]:
        path = os.path.join('./tgbot/middlewares/', file_name + '.py')
        if not os.path.exists(path):
            middleware.create(path, file_name, middleware_types)
            print(f'{file_name} middleware is created')
        else:
            print(f'{file_name} middleware already exists')

    case ['create', 'handler', file_name]:
        path = os.path.join('./', file_name)
        if not os.path.exists(path):
            handler.create(path, file_name)
            print(f'{file_name} handler is created')
        else:
            print(f'{file_name} handler already exists')

    case ['help']:
        print(help_text)

    case _:
        print(f'Not found command. {help_text}')
