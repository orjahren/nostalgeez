# https://stackoverflow.com/a/75292843
from flask import Flask, request, redirect
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
import requests
import json

from config import get_api_client
from user_token import set_user_token


app = Flask(__name__)

# TODO: Should be in config file.
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
REDIRECT_URI = 'http://127.0.0.1:3000/callback'
CLIENT_ID, CLIENT_SECRET = get_api_client()

SCOPE = [
    "user-read-email",
    "playlist-read-collaborative",
    "user-read-playback-state",
    "user-modify-playback-state"
]


@app.route("/")
def index():
    return "<button onclick='window.location=\"/login\"')>Click here to authenticate</button>"


@app.route("/login")
def login():
    spotify = OAuth2Session(CLIENT_ID, scope=SCOPE, redirect_uri=REDIRECT_URI)
    authorization_url, state = spotify.authorization_url(AUTH_URL)
    return redirect(authorization_url)


@app.route("/callback", methods=['GET'])
def callback():
    code = request.args.get('code')
    res = requests.post(TOKEN_URL,
                        auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
                        data={
                            'grant_type': 'authorization_code',
                            'code': code,
                            'redirect_uri': REDIRECT_URI
                        })

    print("*** AUTH: Setting global user token on callback")
    set_user_token(res.json())

    return json.dumps(res.json())


if __name__ == '__main__':
    app.run(port=3000, debug=True)
