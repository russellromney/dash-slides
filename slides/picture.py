# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app

###

content = html.Div(
    style=dict(textAlign="center"),
    children=[
        html.H1("A Slide for a Picture"),
        html.Img(src="https://picsum.photos/id/222/800/600"),
    ],
)
