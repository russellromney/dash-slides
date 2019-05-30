# necessary imports - do not change
import dash_html_components as html
from app import app
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
#

# custom imports
from custom_utilities.custom_functions import print_lorem_ipsum, new_random_colors
from dash import no_update
import dash_bootstrap_components as dbc

content_page_style = dict(textAlign='center',margin='20px')

content = html.Div([
    html.H1('A slide for a random lorem ipsum',style=content_page_style),
    html.Div(
        dbc.Button(children='Generate a new random lorem ipsum!',id='template-content-button',n_clicks=0,color='primary'),
        style=content_page_style
    ),
    dbc.Container(id='template-content',children=print_lorem_ipsum(),style=new_random_colors()),
    html.Div(['Thanks to the folks at Loripsum.net for the cool API! ',html.A('loripsum.net',href='https://loripsum.net/')],style=content_page_style)
])

@app.callback(
    [Output('template-content','children'),
     Output('template-content','style')],
    [Input('template-content-button','n_clicks')]
)
def generate_template_content(n):
    '''returns a random lorem ipsum with a random transparent background color'''
    if n==0:
        return no_update,no_update
    return print_lorem_ipsum(), new_random_colors()