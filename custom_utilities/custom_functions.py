import requests
import random

# file for custom functions


def my_function():
    return 0


def print_lorem_ipsum():
    r = requests.get(
        "https://baconipsum.com/api/?type=meat-and-filler&paras=5&start-with-lorem=1"
    )
    # r = requests.get('https://loripsum.net/api/20/medium/plaintext')
    return r.json()


def new_random_colors():
    return dict(
        background="rgba({},{},{},.9)".format(
            *[random.randint(100, 255) for x in range(3)]
        ),
        maxWidth="700px",
        textAlign="center",
        margin="auto",
    )
