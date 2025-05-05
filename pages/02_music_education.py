import dash
from dash import html, callback, MATCH
import dash_bootstrap_components as dbc

from dash import Dash, dcc, html, Input, Output, State

from utils.helper import make_toast
from utils.manager import data_manager


# initialize app
page_id = "music_education"
dash.register_page(__name__,
                   path='/' + page_id,
                   title='Music Education Questions',
                   name='Your Music Education'
                   )

# set app layout
layout = dbc.Container(children=[
    dcc.Location(id='url'),
    # set app layout
    html.Div([
        html.Div(id="hidden_div_for_redirect_callback_music_education"),
        html.Div(children=[
            html.Br(),
            html.Br(),
            html.H1('Music Education Background', id='title_music_education', style={'textAlign': 'center'}),
            html.Br(),
            html.Br(),
            html.P('I can play an instrument.', {"type": "label", "index": "play_instrument"}),
            dbc.RadioItems(
                id={"type": "slider", "index": "play_instrument"},
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=[
                    {"label": "0 (not at all)", "value": 0},
                    {"label": "1", "value": 1},
                    {"label": "2", "value": 2},
                    {"label": "3", "value": 3},
                    {"label": "4", "value": 4},
                    {"label": "5", "value": 5},
                    {"label": "6 (professional)", "value": 6},
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
            html.P('I have spent ... studying an instrument (formal or informal)'),
            dbc.Select(
                id='instrument_studying',
                options=['Never studied an instrument.',
                         'less than 1 year',
                         'between 1 year to 2 years',
                         'between 2 years and 3 years',
                         'between 3 years and 5 years',
                         'more than 5 years']
            ),
            html.Br(),
            html.P('I had musical education for ...'),
            dbc.Select(
                id='music_education',
                options=['Never had musical education.',
                         'less than 1 year',
                         'between 1 year to 2 years',
                         'between 2 years and 3 years',
                         'between 3 years and 5 years',
                         'more than 5 years']
            ),
            html.Br(),
            dbc.Button('Next', id='start', n_clicks=0,
                       style={'textAlign': 'center',
                              'width': 'auto',
                              'padding-left': '5vw',
                              'padding-right': '5vw',
                              'horizontalAlign': 'right'})
        ], style={'padding': 32, 'flex': 1})
    ], style={'display': 'flex',
              'flex-direction': 'row',
              'padding-left': 'max(calc(50% - 400px), 2%)',
              'padding-right': 'max(calc(50% - 400px), 2%)',
              }),
    html.Div(id='container-button-basic'),
    html.Div(
        id="toast-container-me",
        style={"position": "fixed",
               "top": 10,
               "right": 10,
               "width": 350},
    ),
], className="dbc")


@callback(
    [Output("hidden_div_for_redirect_callback_music_education", "children"),
     Output("toast-container-me", "children"),
     Output('start', 'n_clicks')],
    [State('user_id', 'data'),
     Input('start', 'n_clicks'),
     State('music_education', 'value'),
     State('instrument_studying', 'value'),
     State({"type": "slider", "index": "play_instrument"}, 'value')]
)
def go_to_next_page(code, n_clicks, music_education, instrument_playing, prof_instrument):
    if n_clicks > 0:

        if prof_instrument is None or instrument_playing is None or music_education is None:
            return None, make_toast("Please select an answer for every question.", "music_notice"), 0

        data_manager.save_data(user_id=code,
                               session_id="code",
                               data={"play_instrument": prof_instrument,
                                                 "study_instrument": instrument_playing,
                                                 "music_education": music_education},
                               collection=page_id)

        return dcc.Location(pathname="/music_listening_preferences", id="music_listening_id"), None, 0
    return None, None, 0
