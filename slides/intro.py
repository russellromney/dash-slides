# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app

# custom imports
# ...


content = html.Div(
    style=dict(textAlign="center"),
    children=[
        html.H1("Intro Slide Title"),
        html.Button("Click this!", id="intro-button", n_clicks=0),
        html.H2(id="intro-div"),
        html.Br(),
        html.Div(
            html.Img(
                src="https://cdn-images-1.medium.com/max/2600/1*tJGJzsEJJM21-3LT1XZbyw.jpeg",
                style=dict(height="300px"),
            )
        ),
    ],
)


@app.callback(Output("intro-div", "children"), [Input("intro-button", "n_clicks")])
def create_template_graph(n):
    return "Button has been clicked {} times.".format(n)
