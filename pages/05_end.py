import secrets

import dash
from dash import callback, no_update, State
import dash_bootstrap_components as dbc
from utils.manager import tracker, data_manager

from dash import dcc, html, Input, Output

# initialize app
page_id = "end_questionnaire"
dash.register_page(__name__, path="/" + page_id, title="Start Questionnaire")

# set app layout
layout = dbc.Container(children=[
    dcc.Location(id=page_id + '_url_home'),
    html.Div(id=page_id + "_home_redirect_div"),
    # set app layout
    html.Div([
        html.Div(children=[
            #home page with instructions
            html.Br(),
            html.Br(),
            html.H2('End Questionnaire', style={'textAlign': 'center'}),
            html.Br(),
            html.Br(),
            html.Div([
                html.P('I payed close attention to the music (active listening) or rather not (passive listening).',
                       {"type": "label", "index": 'focus_listening_01'}, style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                html.P(children='(1 = "Passive Listening.", and 10 = "Active Listening")',
                       style={'fontSize': 'small', 'color': 'gray', 'marginTop': '0px'}),
            ], style={'textAlign': 'center'}),
            dbc.RadioItems(
                id={"type": "slider", "index": 'focus_listening'},
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
                html.P(children='My happiness right now', style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                html.P(children='(1 = "I am not happy at all.", and 10 = "I am extremely happy.")',
                       style={'fontSize': 'small', 'color': 'gray', 'marginTop': '0px'}),
            ], style={'textAlign': 'center'}),
            dbc.RadioItems(
                id={"type": "slider", "index": 'happy_end'},
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
                id={"type": "slider", "index": 'sad_end'},
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
            ], style={'textAlign': 'center'}), dbc.RadioItems(
                id={"type": "slider", "index": 'stressed_end'},
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
                id={"type": "slider", "index": 'energy_end'},
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
            dcc.Link(dbc.Button('Next', id=page_id + '_next', n_clicks=0,
                       style={'textAlign': 'center',
                              'width': 'auto',
                              'padding-left': '5vw',
                              'padding-right': '5vw',
                              'horizontalAlign': 'center'}), href="/thank_you", refresh=True),
        ], style={'padding': 32, 'flex': 1})
    ], style={'display': 'flex',
              'flex-direction': 'row',
              'textAlign': 'center',
              'horizonAlign': 'center',
              'padding-left': 'max(calc(50% - 400px), 2%)',
              'padding-right': 'max(calc(50% - 400px), 2%)',
              }),
    html.Div(id=page_id + '_container-button-basic'),
    html.Div(
        id=page_id + "_toast_container",
        style={"position": "fixed", "top": 10, "right": 10, "width": 350},
    ),
])

@callback(
    [Output(page_id + '_next', 'n_clicks'),
     Output(page_id + "_toast_container", "children")],
    [State('user_id', 'data'),
     State('session_id', 'data'),
     Input(page_id + '_next', 'n_clicks'),
     State({"type": "slider", "index": 'happy_end'}, 'value'),
     State({"type": "slider", "index": 'sad_end'}, 'value'),
     State({"type": "slider", "index": 'stressed_end'}, 'value'),
     State({"type": "slider", "index": 'energy_end'}, 'value'),
     State({"type": "slider", "index": 'focus_listening'}, 'value')
     ]
)
def go_to_next_page(code, session_id, n_clicks,
                    happy_start,
                    sad_start,
                    stressed_start,
                    energy_start,
                    focus
                    ):
    if n_clicks > 0:
        # This is done so that we can be sure that the saving works when they click further.
        # If an error appears they won't be able to continue.
        print("Code: ", code, "Session Id: ", session_id)
        saved = data_manager.save_data(user_id=code, session_id=session_id,
                                       data={"happy": happy_start,
                                             "sad": sad_start,
                                             "stressed": stressed_start,
                                             "energy": energy_start,
                                             "focus": focus},
                                       collection="end")
        if saved:
            print("saved..", code),
            return 0, no_update

        else:
            print("Error while saving..", code)
            return 0, no_update

    return 0, no_update
