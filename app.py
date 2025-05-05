import dash
import dash_bootstrap_components as dbc
import flask

from dash import html, dcc

# initialize app

server = flask.Flask(__name__)

app = dash.Dash(server=server, external_stylesheets=[dbc.themes.SANDSTONE], use_pages=True)

# set app layout
app.layout = html.Div(children=[
    dcc.Store(id="user_id", data=None, storage_type='session'),
    dcc.Store(id="session_id", data=None, storage_type='session'),
    dcc.Store(id="last_fm_username", storage_type='session'),
    dcc.Store(id="context_information", data={}, storage_type='session'),
    dcc.Store(id="session_tracks", data=[], storage_type='session'),
    dash.page_container,
])


if __name__ == "__main__":
    #print("Start.")
    app.run(host="0.0.0.0")
