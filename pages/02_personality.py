import dash
from dash import html, callback
import dash_bootstrap_components as dbc

from dash import Dash, dcc, html, Input, Output, State

from utils.manager import data_manager
from utils.helper import make_toast

options = [
    {"label": "Strongly Disagree", "value": 0},
    {"label": "Disagree", "value": 1},
    {"label": "Somewhat Disagree", "value": 2},
    {"label": "Neutral", "value": 3},
    {"label": "Somewhat Agree", "value": 4},
    {"label": "Agree", "value": 5},
    {"label": "Agree Strongly", "value": 6},
]

# initialize app
page_id = "personality"
dash.register_page(__name__,
                   path='/' + page_id,
                   title='Personality Questions',
                   name='Your Personality'
                   )

# set app layout
layout = dbc.Container(children=[
    dcc.Location(id='url'),
    # set app layout
    html.Div([
        html.Div(id="hidden_div_for_redirect_callback_personality"),
        html.Div(children=[
            html.Br(),
            html.Br(),
            html.H1('Personality Questions', id='title_personality', style={'textAlign': 'center'}),
            html.Br(),
            html.Br(),
            html.P('I see myself as extroverted, enthusiastic.', {"type": "label", "index": 'extroverted'}),
            dbc.RadioItems(
                id={"type": "slider", "index": 'extroverted'},
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=options,
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
            html.P('I see myself as critical, quarrelsome.', {"type": "label", "index": 'critical'}),
            dbc.RadioItems(
                id={"type": "slider", "index": 'critical'},
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=options,
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
            html.P('I see myself as dependable, self-disciplined.', {"type": "label", "index": 'dependable'}),
            dbc.RadioItems(
                id={"type": "slider", "index": 'dependable'},
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=options,
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
            html.P('I see myself as anxious, easily upset.', {"type": "label", "index": 'anxious'}),
            dbc.RadioItems(
                id={"type": "slider", "index": 'anxious'},
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=options,
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
            html.P('I see myself as open to new experiences, complex.', {"type": "label", "index": 'openess'}),
            dbc.RadioItems(
                id={"type": "slider", "index": 'openess'},
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=options,
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
            html.P('I see myself as reserved, quiet.', {"type": "label", "index": 'reserved'}),
            dbc.RadioItems(
                id={"type": "slider", "index": 'reserved'},
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=options,
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
            html.P('I see myself as sympathetic, warm.', {"type": "label", "index": 'sympathetic'}),
            dbc.RadioItems(
                id={"type": "slider", "index": 'sympathetic'},
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=options,
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
            html.P('I see myself as disorganized, careless.', {"type": "label", "index": 'disorganized'}),
            dbc.RadioItems(
                id={"type": "slider", "index": 'disorganized'},
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=options,
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
            html.P('I see myself as calm, emotionally stable.', {"type": "label", "index": 'calm'}),
            dbc.RadioItems(
                id={"type": "slider", "index": 'calm'},
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=options,
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
            html.P('I see myself as conventional, uncreative.', {"type": "label", "index": 'conventional'}),
            dbc.RadioItems(
                id={"type": "slider", "index": 'conventional'},
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=options,
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
            html.Br(),
            dbc.Button('Next', id='start_personality', n_clicks=0,
                       style={'textAlign': 'center',
                              'width': 'auto',
                              'padding-left': '5vw',
                              'padding-right': '5vw',
                              'horizontalAlign': 'center'})
        ], style={'padding': 32, 'flex': 1})
    ], style={'display': 'flex',
              'flex-direction': 'row',
              'padding-left': 'max(calc(50% - 400px), 2%)',
              'padding-right': 'max(calc(50% - 400px), 2%)',
              }),
    html.Div(id='container-button-basic'),
    html.Div(
        id="toast-container-pe",
        style={"position": "fixed",
               "top": 10,
               "right": 10,
               "width": 350},
    ),
])

@callback(
    [Output("hidden_div_for_redirect_callback_personality", "children"),
     Output("start_personality", 'n_clicks'),
     Output("toast-container-pe", "children"), ],
    [Input('user_id', 'data'),
     Input('start_personality', 'n_clicks'),
     Input({"type": "slider", "index": 'extroverted'}, 'value'),
     Input({"type": "slider", "index": 'critical'}, 'value'),
     Input({"type": "slider", "index": 'dependable'}, 'value'),
     Input({"type": "slider", "index": 'anxious'}, 'value'),
     Input({"type": "slider", "index": 'openess'}, 'value'),
     Input({"type": "slider", "index": 'reserved'}, 'value'),
     Input({"type": "slider", "index": 'sympathetic'}, 'value'),
     Input({"type": "slider", "index": 'disorganized'}, 'value'),
     Input({"type": "slider", "index": 'calm'}, 'value'),
     Input({"type": "slider", "index": 'conventional'}, 'value')]
)
def go_to_next_page(code, n_clicks, extroverted, critical, dependable, anxious, openess, reserved, sympathetic,
                    disorganized, calm, conventional):
    if n_clicks > 0:
        if None in [extroverted, critical, dependable, anxious, openess, reserved, sympathetic, disorganized, calm,
                    conventional]:
            return None, 0, make_toast("Please select an answer for every question.", "music_notice")

        data_manager.save_data(user_id=code, session_id=code,
                               data={"extroverted": extroverted, "critical": critical, "dependable": dependable,
                                             "anxious": anxious, "openess": openess, "reserved": reserved,
                                             "sympathetic": sympathetic, "disorganized": disorganized,
                                             "calm": calm, "conventional": conventional}, collection=page_id)

        return dcc.Location(pathname="/start_questionnaire", id="session_id"), 0, None
    return None, 0, None
