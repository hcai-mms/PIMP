import secrets

import dash
from dash import callback, no_update, State
import dash_bootstrap_components as dbc
from utils.manager import tracker, data_manager
import datetime

from dash import dcc, html, Input, Output

# initialize app
page_id = "session"
dash.register_page(__name__, path="/" + page_id, title="Start Questionnaire")

update_tracks_every_x_seconds = 3

# set app layout
layout = dbc.Container(children=[
    dcc.Location(id=page_id + '_url_home'),
    dcc.Interval(id='interval_reload', interval=update_tracks_every_x_seconds * 1000, n_intervals=0),
    html.Div(id=page_id + "_home_redirect_div"),
    # set app layout
    html.Div([
        html.Div(children=[
            #home page with instructions
            html.Br(),
            html.Br(),
            html.H2('Logging Session', style={'textAlign': 'center'}),
            html.Br(),
            html.Br(),
            html.P("You are currently logging a music listening session. Below you can see all the tracks that have been logged for this session. If you are finished, please click 'Finish Session' to save this session."),
            html.Br(),
            html.Br(),
            dbc.Button('Finish Session', id=page_id + '_next', n_clicks=0,
                       style={'textAlign': 'center',
                              'width': 'auto',
                              'padding-left': '5vw',
                              'padding-right': '5vw',
                              'horizontalAlign': 'center'}),
            html.Br(),
            html.Br(),
            html.H2("Logged Tracks"),
            html.Br(),
            dbc.Container(id=page_id + "_list_tracks", children=[])
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

@callback([Output(page_id + "_list_tracks", "children"),
          Output("session_tracks", "data", allow_duplicate=True)],
          [Input("last_fm_username", "data"),
          Input('interval_reload', 'n_intervals'),
          State(page_id + "_list_tracks", "children"),
          State("session_tracks", "data")],
    prevent_initial_call=True)
def get_new_tracks(username, interval, cur_tracks_shown, cur_tracks_logged):
    tracks = tracker.fetch(username=username)['track']
    tracks.reverse()

    for track in tracks:
        mbid = str(track["mbid"])
        url = str(track["url"])
        song_name = str(track["name"])
        album_name = str(track["album"]["#text"])
        artist = str(track["artist"]["#text"])

        if '@attr' in track and track['@attr'] != None and track["@attr"]["nowplaying"] != None:
            finished = not bool(track['@attr']['nowplaying'])
        else:
            finished = True

        if not finished:
            t = datetime.datetime.now()

            new_track_entry = {
                "pos": len(cur_tracks_logged),
                "mbid": mbid,
                "url": url,
                "song_title": song_name,
                "album_title": album_name,
                "artist_name": artist,
                "finished_listening": finished,
                "listened_for_approx": 0,
                "time_started": t.strftime('%m/%d/%Y %H:%M:%S')
            }

            if len(cur_tracks_logged) > 0:
                last_track = cur_tracks_logged[-1]

                if last_track['url'] is not None and new_track_entry['url'] is not None and last_track['url'] == new_track_entry['url']:
                    # Same track.
                    diff = (t - datetime.datetime.strptime(last_track['time_started'], '%m/%d/%Y %H:%M:%S')).total_seconds()
                    cur_tracks_logged[-1]['listened_for_approx'] = diff
                else:
                    cur_tracks_logged.append(new_track_entry)
            else:
                cur_tracks_logged.append(new_track_entry)
        else:
            if len(cur_tracks_logged) > 0:
                last_track = cur_tracks_logged[-1]

                if last_track['url'] is not None and url is not None and last_track['url'] == url:
                    cur_tracks_logged[-1]['finished_listening'] = True

    children = []

    for t in reversed(cur_tracks_logged):
        s = int(t['listened_for_approx'] * 10) / 10
        children.append(dbc.Container(
            children=[
                html.H4(f"{t['song_title']} - {t['artist_name']}"),
                html.P(f"Finished: {t['finished_listening']}, Listened for : {s} seconds"),
            ],
        ))
        children.append(html.Br())

    return children, cur_tracks_logged


@callback(
    [Output(page_id + "_home_redirect_div", "children"),
        Output(page_id + '_next', 'n_clicks'),
        Output("session_tracks", "data", allow_duplicate=True),
    ],
    [State('user_id', 'data'),
     State('session_id', 'data'),
     Input(page_id + '_next', 'n_clicks'),
     State('session_tracks', 'data')],
    prevent_initial_call=True
)
def go_to_next_page(code, session_id, n_clicks, session_tracks):
    if n_clicks > 0:
        # This is done so that we can be sure that the saving works when they click further.
        # If an error appears they won't be able to continue.
        saved = data_manager.save_data(user_id=code,
                                       session_id=session_id,
                                       data=session_tracks,
                                       collection="tracks_logged")
        if saved:
            #print("saved..", code),
            return dcc.Location(pathname="/end_questionnaire", id="consent_id"), 0, []
        else:
            print("Error while saving..", code)
            return no_update, 0, no_update

    return no_update, 0, no_update
