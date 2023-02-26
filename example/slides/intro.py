# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from app import app


content = html.Div(
    [
        html.H1("This is my intro slide!"),
        html.Div(
            html.Img(
                src="https://cdn-images-1.medium.com/max/2600/1*tJGJzsEJJM21-3LT1XZbyw.jpeg",
                style=dict(height="300px"),
            )
        ),
    ],
    style=dict(textAlign="center"),
)
