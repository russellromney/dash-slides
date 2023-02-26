###
# no need to delete this - it won't show up in the presentation unless you add it to presentation.py
###

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app

# custom imports - delete these if you don't need them
from custom_utilities.custom_functions import my_function

content = html.Div(
    style=dict(textAlign="center"),
    children=[
        html.H1("Template Slide Title"),
        html.Button("Click this!", id="template-button", n_clicks=0),
        html.H2(id="template-div"),
    ],
)


@app.callback(
    Output("template-div", "children"), [Input("template-button", "n_clicks")]
)
def create_template_graph(n):
    return "Button has been clicked {} times.".format(n)
