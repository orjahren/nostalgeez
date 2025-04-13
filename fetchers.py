import requests
import sys
import os
from dotenv import load_dotenv
from functools import lru_cache
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")


# TODO: Invalidate cache based on token validity
@lru_cache
def fetch_access_token():

    print("client id:", CLIENT_ID)
    print("client secret:", CLIENT_SECRET)

    url = f"https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    body = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    print("Fetching access token from net", file=sys.stderr)
    # TODO: Error handling
    res = requests.post(url, data=body, headers=headers)
    print(res.status_code)
    assert res.status_code == 200, "Error fetching access token"
    return res.json()


@lru_cache
def get_access_token():
    response = fetch_access_token()
    return response["access_token"]


@lru_cache
def fetch_artist(artist_id: str, access_token: str) -> object:
    print(f"Fetching artist {artist_id}")
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    r = requests.get(url, headers=headers)
    assert r.status_code == 200, "Error fetching artist"

    return r.json()


"""
if __name__ == "__main__":
    access_token = get_access_token()
    test_artist = "4Z8W4fKeB5YxbusRsdQVPb"
    res = fetch_artist(test_artist, access_token)
    print(res)
    res = fetch_artist(test_artist, access_token)
    print(res)
"""


if __name__ == "__main__":
    access_token = get_access_token()
    print(access_token)
    # NOTE: Should only cause 1 network IO due to LRU cache
    access_token = get_access_token()
    print(access_token)
    access_token = get_access_token()
    print(access_token)
