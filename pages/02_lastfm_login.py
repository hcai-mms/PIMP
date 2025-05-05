import secrets

import dash
from dash import callback, no_update
import dash_bootstrap_components as dbc

from dash import dcc, html, Input, Output, State

from utils.manager import tracker, data_manager

# initialize app
page_id = "lastfm_login"
dash.register_page(__name__, path="/" + page_id, title="Last.FM Login")

# set app layout
layout = dbc.Container(children=[
    dcc.Location(id=page_id + '_url_home'),
    html.Div(id=page_id + "_home_redirect_div"),
    # set app layout
    html.Div([
        html.Div(children=[
            #home page with instructions
            html.H1(children='Last.FM Login', style={'textAlign': 'left'}),
            html.Br(),
            html.P(children='Please login through Last.FM to continue, none of this will be saved.', style={'textAlign': 'left', 'fontWeight': 'bold'}),
            html.P(children="By logging in with Last.FM here, you connect your Last.FM account with this application. Applications are visible in your account here: https://www.last.fm/settings/applications and can be removed at any time. Note, that for this application to work, the application needs to be connected with your Last.FM Account."),
            dbc.Input(
                id=page_id + "_lastfm_username", placeholder="Your Last.FM Username", step=1,
            ),
            html.Br(style={"line-height": "5"}),
            dbc.Input(
                id=page_id + "_lastfm_pwd", placeholder="Your Last.FM Password", type='password'
            ),
            html.Br(),
            html.Br(),
            dbc.Button('Login', id=page_id + '_login', n_clicks=0,
                       style={'textAlign': 'center',
                              'width': 'auto',
                              'padding-left': '5vw',
                              'padding-right': '5vw',
                              'horizontalAlign': 'center'})
        ], style={'padding': 32, 'flex': 1})
    ], style={'display': 'flex',
              'flex-direction': 'row',
              'textAlign': 'center',
              'horizonAlign': 'center',
              'padding-left': 'max(calc(50% - 400px), 2%)',
              'padding-right': 'max(calc(50% - 400px), 2%)',
              }),
    html.Div(
        id=page_id + "_toast_container",
        style={"position": "fixed", "top": 10, "right": 10, "width": 350},
    ),
])

@callback(
    [Output(page_id + "_home_redirect_div", "children"),
        Output(page_id + '_login', 'n_clicks'),
     Output(page_id + "_toast_container", "children"),
     Output("last_fm_username", "data")],
    [State('user_id', 'data'),
     Input(page_id + '_login', 'n_clicks'),
     State(page_id + '_lastfm_username', 'value'),
     State(page_id + '_lastfm_pwd', 'value'),]
)
def go_to_next_page(code, n_clicks, username, pwd):
    if n_clicks > 0:

        if username is None or len(username) < 0 or pwd is None or len(pwd) < 0:
            return no_update, 0, dbc.Toast("Please enter all your credentials.", color="danger", duration=3000), no_update

        # This is done so that we can be sure that the saving works when they click further.
        # If an error appears they won't be able to continue.

        tracker.login(username=username, password=pwd)
        #print("saved..", code),
        if data_manager.check_if_exists(code=code, collection="personality"):
            return dcc.Location(pathname="/start_questionnaire", id="consent_id"), 0, no_update, username
        else:
            return dcc.Location(pathname="/demographic_information", id="consent_id"), 0, no_update, username

    return no_update, 0, no_update, no_update
