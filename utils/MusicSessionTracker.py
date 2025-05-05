import os
import pylast
import requests


class MusicListeningSession:
    def __init__(self):
        self.activity = None
        self.social = None
        self.motivation = None
        self.mood = None



class LastFMTracker:

    def __init__(self):
        self.lfm_apikey = os.environ['LASTFM_API_KEY']
        self.lfm_apisecret = os.environ['LASTFM_API_SECRET']
        self.network = None
        self.session = []

        print("Api Key: ", self.lfm_apikey)
        print("Api secret: ", self.lfm_apisecret)

    def login(self, username, password):
        self.network = pylast.LastFMNetwork(
            api_key=self.lfm_apikey,
            api_secret=self.lfm_apisecret,
            username=username,
            password_hash=pylast.md5(password),
        )

    def start_session(self):
        self.session = []

    def fetch(self, username):
        request = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks"
        request += "&user=" + username
        request += "&api_key=" + self.lfm_apikey
        request += "&limit=5"
        request += "&format=json"

        response = requests.post(request)
        tracks = response.json()
        return tracks['recenttracks']