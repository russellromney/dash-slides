# file for custom functions

import requests
import dash_html_components as html
from random import randrange


def print_lorem_ipsum():
    '''prints a random lorem ipsum'''
    text = requests.get('https://loripsum.net/api/plaintext')
    return html.Div([
        html.H4('Internet text!'),
        *[html.P(s) for s in text.text.split('\n')]
    ])

def new_random_colors():
    random_colors = [randrange(0,255) for i in range(3)]
    random_colors = 'rgba({},{},{},.1)'.format(*random_colors)
    return dict(backgroundColor=random_colors)