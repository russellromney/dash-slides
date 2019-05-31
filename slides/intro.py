# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
import dash_html_components as html
from app import app
import dash_core_components as dcc
from dash.dependencies import Output, Input, State

# custom imports
# ...


content = html.Div(style=dict(textAlign='center'),children=[
    html.H1('Intro Slide Title'),
    html.Button('Click this!',id='intro-button',n_clicks=0),
    html.H2(id='intro-div')
])


@app.callback(
    Output('intro-div','children'),
    [Input('intro-button','n_clicks')]
)
def create_template_graph(n):
    return 'Button has been clicked {} times.'.format(n)