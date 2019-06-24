# necessary imports - do not change
import dash_html_components as html
from app import app
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
###

content = html.Div(style=dict(textAlign='center'),children=[
    html.H1('A Slide for a Picture'),
    html.Img(src='https://picsum.photos/id/222/800/600')
])