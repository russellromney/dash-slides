# necessary imports - do not change
import dash_html_components as html
from app import app
import dash_core_components as dcc
from dash.dependencies import Output, Input, State


content = html.Div(
    [
        html.H1('This is my intro slide!'),
        html.Div(
            html.Img(
                src='https://cdn-images-1.medium.com/max/2600/1*tJGJzsEJJM21-3LT1XZbyw.jpeg',
                style=dict(height='300px')
            )
        )
    ],
    style=dict(textAlign='center')
)