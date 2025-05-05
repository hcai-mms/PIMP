import dash
import dash_bootstrap_components as dbc

from dash import dcc, html

#
# initialize app
page_id = "thank_you"
dash.register_page(__name__, path="/" + page_id,
                   title='Thank you')
#
# set app layout
layout = dbc.Container(children=[
    dcc.Location(id='url_thank_you'),
    html.Div(id="thank_you_redirect_div"),
    html.Div([
        html.Div(children=[
#
            html.Br(),
            html.H1(children='Thank you for your participation!', style={'textAlign': 'left'}),
            html.Br(),
            html.P("Your session has been saved successfully! If you want to log another session just reenter at the home page."),
            html.P('Everything has been saved and you can exit the page.',
                   style={'textAlign': 'left'}),
            html.Br(),
#
        ], style={'padding': 32, 'flex': 1})
    ], style={'display': 'flex',
              'flex-direction': 'row',
              'textAlign': 'left',
              'horizonAlign': 'left',
              'padding-left': 'max(calc(50% - 400px), 2%)',
              'padding-right': 'max(calc(50% - 400px), 2%)',
              }),
    html.Div(
        id="toast_container_thank_you",
        style={
            "position": "fixed",
            "color": "red",
            "font-weight": "bold",
            "top": 200,
            "left": 200,
            "width": 350},
    ),
])
#
