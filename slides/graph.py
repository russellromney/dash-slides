# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app

# custom imports
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from dash import no_update
from random import randrange

content = html.Div(
    style=dict(textAlign="center"),
    children=[
        html.H1("Template Slide Title"),
        dcc.Markdown(
            """
This is template content!
    """
        ),
        dbc.Button(
            "Click this to change the graph!",
            id="template-button",
            n_clicks=0,
            color="primary",
        ),
        dcc.Graph(id="template-graph"),
        dcc.Markdown(
            """
This is more template content
    """
        ),
    ],
)


@app.callback(
    Output("template-graph", "figure"), [Input("template-button", "n_clicks")]
)
def create_template_graph(n):
    x_data = list(range(50))
    y_data = [i + randrange(-10, 10) for i in range(50)]
    data = [go.Scatter(x=x_data, y=y_data)]
    layout = go.Layout(title="Template Graph Title")
    return go.Figure(data, layout)
