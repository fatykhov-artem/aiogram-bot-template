import os

import tgbot.aiotelegraph.view as view


def example_view():
    messages_text = view.text('example')

    text = messages_text['title']
    markup = []
    
    # You code
    
    return text, markup
