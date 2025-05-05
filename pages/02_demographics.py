import secrets

import dash
from dash import html, callback, no_update
import dash_bootstrap_components as dbc
from utils.manager import data_manager

import pycountry

from dash import Dash, dcc, html, Input, Output, State

# VARIABLES
all_countries = [c.name for c in list(pycountry.countries)]
all_countries.sort()

# initialize app
page_id = "demographic_information"
dash.register_page(__name__, path="/" + page_id)

# set app layout
layout = dbc.Container(children=[
    dcc.Location(id='url_demographic_info'),
    html.Div(id="demographic_info_redirect_div"),
    html.Div([
        html.Div(children=[
            html.H1(children='Demographic information', style={'textAlign': 'left'}),
            html.Br(),
            html.P(children='What is your age?', style={'textAlign': 'left', 'fontWeight': 'bold'}),
            dbc.Input(
                id="user_age", type="number", placeholder="age as a number",
                step=1,
            ),
            html.Br(),
            html.Br(),
            html.P(children='What is your gender?', style={'textAlign': 'left', 'fontWeight': 'bold'}),
            dbc.Select(['Female', 'Male', 'Other'], '', id='user_gender'),
            html.Br(),
            html.P('In which country were you born?', style={'textAlign': 'left', 'fontWeight': 'bold'}),
            dbc.Select(
                id='birth_country',
                options=all_countries
            ),
            html.Br(),
            html.P('In which country do you live right now?', style={'textAlign': 'left', 'fontWeight': 'bold'}),
            dbc.Select(
                id='residence_country',
                options=all_countries
            ),
            html.Br(),
            dbc.Button('Next page', id='next_from_demographic', n_clicks=0,
                       style={'textAlign': 'center',
                              'width': 'auto',
                              'padding-left': '5vw',
                              'padding-right': '5vw',
                              'horizontalAlign': 'center'})

        ], style={'padding': 32, 'flex': 1})
    ], style={'display': 'flex',
              'flex-direction': 'row',
              'textAlign': 'left',
              'horizonAlign': 'left',
              'padding-left': 'max(calc(50% - 400px), 2%)',
              'padding-right': 'max(calc(50% - 400px), 2%)',
              }),
    html.Div(
        id="toast_container_demographic_info",
        style={"position": "fixed",
               "color": "red",
               "font-weight": "bold",
               "top": 200,
               "left": 200,
               "width": 350},
    ),
])
@callback(
    [Output("demographic_info_redirect_div", "children"),
     Output('next_from_demographic', 'n_clicks'),
     Output('toast_container_demographic_info', 'children')],
    [State('user_id', 'data'),
     Input('next_from_demographic', 'n_clicks'),
     State('user_age', 'value'),
     State('user_gender', 'value'),
     State('birth_country', 'value'),
     State('residence_country', 'value')]
)
def go_to_next_page(code, n_clicks, user_age, user_gender, birth_country, residence_country):

    if n_clicks > 0:
        data_manager.save_data(user_id=code,
                               session_id=code,
                               data={
                                    'code': code,
                                    'user_age': user_age,
                                    'user_gender': user_gender,
                                    'birth_country': birth_country,
                                    'residence_country': residence_country,
                                }, collection=page_id),
        if None in [user_age, user_gender, birth_country, residence_country]:
            print([user_age, user_gender, birth_country, residence_country])
            return None, 0, dbc.Toast([html.P("Please fill in all fields")]),
        else:
            return dcc.Location(pathname="/music_education", id="id_music_listening_behavior"), 0, None,
    return None, 0, None,

# Input('passive_listening_week', 'value')