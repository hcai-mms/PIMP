import secrets
from datetime import datetime

import dash
from dash import callback, no_update
import dash_bootstrap_components as dbc

from dash import dcc, html, Input, Output, State

from utils.manager import tracker, data_manager

# initialize app
page_id = ""
dash.register_page(__name__, path="/" + page_id, title="Home")

# set app layout
layout = dbc.Container(children=[
    dcc.Location(id=page_id + '_url_home'),
    html.Div(id="home_redirect_div"),
    # set app layout
    html.Div([
        html.Div(children=[
            #home page with instructions
            html.Br(),
            html.Br(),
            html.H2('Last.FM Tracking Music Listening Sessions', style={'textAlign': 'center'}),
            html.Br(),
            #html.P("It is strongly advised to user a laptop for this survey.",
            #       style={'textAlign': 'center', 'fontWeight': 'bold'}),
            html.Br(),
            html.P("This dashboard allows you to track music listening sessions with Last.FM.", style={'textAlign': 'left'}),
            html.P("Choose a unique name to track your music listening session and then continue.", style={'textAlign': 'left'}),
            dbc.Input(
                id="unique_id", placeholder="Your Experiment Identification", step=1,
            ),
            dcc.Link(dbc.Button('Next', id=page_id + '_test_save', n_clicks=0,
                       style={'textAlign': 'center',
                              'width': 'auto',
                              'padding-left': '5vw',
                              'padding-right': '5vw',
                              'horizontalAlign': 'center'}), href="/lastfm_login", refresh=False),
        ], style={'padding': 32, 'flex': 1})
    ], style={'display': 'flex',
              'flex-direction': 'row',
              'textAlign': 'center',
              'horizonAlign': 'center',
              'padding-left': 'max(calc(50% - 400px), 2%)',
              'padding-right': 'max(calc(50% - 400px), 2%)',
              }),
    html.Div(id='container-button-basic'),
    html.Div(
        id="toast-container",
        style={"position": "fixed", "top": 10, "right": 10, "width": 350},
    ),
])

@callback(
    Output(page_id + '_url_home', "search"),
    Input("user_id", "data")
)
def adjust_search(idx):
    return f"code={idx}"

@callback(
    [Output('user_id', "data"),
        Output("session_id", "data"),
        Output(page_id + '_test_save', 'n_clicks'),],
    [Input(page_id + '_test_save', 'n_clicks'),
     State("unique_id", "value")]
)
def go_to_next_page(n_clicks, code):
    if n_clicks > 0:
        # This is done so that we can be sure that the saving works when they click further.
        # If an error appears they won't be able to continue.
        t = datetime.now()
        session_id = t.strftime('%m-%d-%Y %H:%M:%S')
        print("Session ID: ", session_id)

        saved = data_manager.save_data(user_id=code,
                                       session_id=session_id,
                                       data={"test": n_clicks},
                                       collection="test")
        if saved:
            #print("saved..", code),
            print("Go to next")
            return code, session_id, 0
        else:
            print("Error while saving..", code)
            return no_update, no_update, 0

    return no_update, no_update, 0
