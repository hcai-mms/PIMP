import secrets

import dash
from dash import callback, no_update, State
import dash_bootstrap_components as dbc
from utils.manager import tracker, data_manager

from dash import dcc, html, Input, Output

# initialize app
page_id = "start_questionnaire"
dash.register_page(__name__, path="/" + page_id, title="Start Questionnaire")

# set app layout
layout = dbc.Container(children=[
    dcc.Location(id='url_start'),
    dcc.Interval(id='reload_start', interval=10 * 1000),
    # set app layout
    html.Div([
        html.Div(id="hidden_div_for_redirect_callback_session_start"),
        html.Div(children=[
            html.Br(),
            html.Br(),
            html.H1('Start Session Questionnaire', style={'textAlign': 'center'}),
            html.Br(),
            html.Br(),
            html.Div([
                html.P(children='My happiness right now', style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                html.P(children='(1 = "I am not happy at all.", and 10 = "I am extremely happy.")',
                    style={'fontSize': 'small', 'color': 'gray', 'marginTop': '0px'}),
            ], style={'textAlign': 'center'}),
            dbc.RadioItems(
                id={"type": "slider", "index": 'happy_start'},
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=[
                    {"label": "1", "value": 1},
                    {"label": "2", "value": 2},
                    {"label": "3", "value": 3},
                    {"label": "4", "value": 4},
                    {"label": "5", "value": 5},
                    {"label": "6", "value": 6},
                    {"label": "7", "value": 7},
                    {"label": "8", "value": 8},
                    {"label": "9", "value": 9},
                    {"label": "10", "value": 10},
                ],
                value=None,
                style={"width": "100%",
                       "display": 'flex',
                       "flex-direction": 'row',
                       'justify': 'center',
                       'justify-content':
                           'space-between',
                       'align-items': 'center'},
            ),
            html.Br(),
            html.Br(),
            html.Div([
                html.P(children='My sadness right now', style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                html.P(children='(1 = "I am not sad at all.", and 10 = "I am extremely sad.")',
                       style={'fontSize': 'small', 'color': 'gray', 'marginTop': '0px'}),
            ], style={'textAlign': 'center'}),
            dbc.RadioItems(
                id={"type": "slider", "index": 'sad_start'},
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=[
                    {"label": "1", "value": 1},
                    {"label": "2", "value": 2},
                    {"label": "3", "value": 3},
                    {"label": "4", "value": 4},
                    {"label": "5", "value": 5},
                    {"label": "6", "value": 6},
                    {"label": "7", "value": 7},
                    {"label": "8", "value": 8},
                    {"label": "9", "value": 9},
                    {"label": "10", "value": 10},
                ],
                value=None,
                style={"width": "100%",
                       "display": 'flex',
                       "flex-direction": 'row',
                       'justify': 'center',
                       'justify-content':
                           'space-between',
                       'align-items': 'center'},
            ),
            html.Br(),
            html.Br(),
            html.Div([
                html.P(children='My stress right now', style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                html.P(children='(1 = "I am not stressed at all.", and 10 = "I am extremely stressed.")',
                       style={'fontSize': 'small', 'color': 'gray', 'marginTop': '0px'}),
            ], style={'textAlign': 'center'}),
            dbc.RadioItems(
                id={"type": "slider", "index": 'stressed_start'},
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=[
                    {"label": "1", "value": 1},
                    {"label": "2", "value": 2},
                    {"label": "3", "value": 3},
                    {"label": "4", "value": 4},
                    {"label": "5", "value": 5},
                    {"label": "6", "value": 6},
                    {"label": "7", "value": 7},
                    {"label": "8", "value": 8},
                    {"label": "9", "value": 9},
                    {"label": "10", "value": 10},
                ],
                value=None,
                style={"width": "100%",
                       "display": 'flex',
                       "flex-direction": 'row',
                       'justify': 'center',
                       'justify-content':
                           'space-between',
                       'align-items': 'center'},
            ),
            html.Br(),
            html.Br(),
            html.Div([
                html.P(children='My energy right now', style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                html.P(children='(1 = "I am out of energy.", and 10 = "I am full with energy.")',
                       style={'fontSize': 'small', 'color': 'gray', 'marginTop': '0px'}),
            ], style={'textAlign': 'center'}),
            dbc.RadioItems(
                id={"type": "slider", "index": 'energy_start'},
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=[
                    {"label": "1", "value": 1},
                    {"label": "2", "value": 2},
                    {"label": "3", "value": 3},
                    {"label": "4", "value": 4},
                    {"label": "5", "value": 5},
                    {"label": "6", "value": 6},
                    {"label": "7", "value": 7},
                    {"label": "8", "value": 8},
                    {"label": "9", "value": 9},
                    {"label": "10", "value": 10},
                ],
                value=None,
                style={"width": "100%",
                       "display": 'flex',
                       "flex-direction": 'row',
                       'justify': 'center',
                       'justify-content':
                           'space-between',
                       'align-items': 'center'},
            ),
            html.Br(),
            html.Br(),
            html.P('What are you doing?'),
            dbc.Checklist(
                options=["waking up",
                         "bathing",
                         "doing sports",
                         "working",
                         "doing housework",
                         "relaxing",
                         "eating",
                         "showering",
                         "playing",
                         "as background when socializing",
                         "as background for romantic company",
                         "while reading",
                         "going to sleep",
                         "driving",
                         "riding a train, bus or plane",
                         'other'],
                value=[],
                id="activity"
            ),
            html.Br(),
            html.Br(),
            html.P('Who are you with?'),
            dbc.Checklist(
                options=['alone',
                         'with friends',
                         'with colleagues',
                         'with family',
                         'with partner or boy/girlfriend',
                         'other'],
                value=[],
                id="social_context"
            ),
            html.Br(),
            html.Br(),
            html.P('What is your current main motivation for listening to music?'),
            dbc.Checklist(
                ['To help me reflect about myself.',
                 'To regulate my mood.',
                 'To feel connected to my friends or social group.',
                 'Just for entertainment.'
                 ],
                [],
                id='motivation'
            ),
            html.Br(),
            html.Br(),
            dbc.Button('Next', id='next_start', n_clicks=0,
                       style={'textAlign': 'center',
                              'width': 'auto',
                              'padding-left': '5vw',
                              'padding-right': '5vw',
                              'horizontalAlign': 'center',
                              })
        ], style={'padding': 32, 'flex': 1})
    ], style={'display': 'flex',
              'flex-direction': 'row',
              'padding-left': 'max(calc(50% - 400px), 2%)',
              'padding-right': 'max(calc(50% - 400px), 2%)',
              }),
    html.Div(id='container-button-basic'),
    html.Div(
        id="toast-container-start",
        style={"position": "fixed",
               "top": 10,
               "right": 10,
               "width": 350},
    ),
])


@callback(
    [Output("hidden_div_for_redirect_callback_session_start", "children"),
     Output('next_start', 'n_clicks'),
     Output("toast-container-start", "children")],
    [State('user_id', 'data'),
     State('session_id', 'data'),
     Input('next_start', 'n_clicks'),
     State({"type": "slider", "index": 'happy_start'}, 'value'),
     State({"type": "slider", "index": 'sad_start'}, 'value'),
     State({"type": "slider", "index": 'stressed_start'}, 'value'),
     State({"type": "slider", "index": 'energy_start'}, 'value'),
     State('activity', 'value'),
     State('social_context', 'value'),
     State('motivation', 'value')
     ]
)
def go_to_next_page(code, session_id, n_clicks,
                    happy_start,
                    sad_start,
                    stressed_start,
                    energy_start,
                    activity,
                    social,
                    motivation
                    ):
    if n_clicks > 0:
        # This is done so that we can be sure that the saving works when they click further.
        # If an error appears they won't be able to continue.
        print("code: ", code)
        print("Session ID: ", session_id)
        saved = data_manager.save_data(user_id=code, session_id=session_id,
                                       data={"activity": activity,
                                             "social": social,
                                             "motivation": motivation,
                                             "happy": happy_start,
                                             "sad": sad_start,
                                             "stressed": stressed_start,
                                             "energy": energy_start},
                                       collection="start")
        if saved:
            #print("saved..", code),
            return dcc.Location(pathname="/session", id="id_session"), 0, no_update

        else:
            print("Error while saving..", code)
            return no_update, 0, no_update

    return no_update, 0, no_update
