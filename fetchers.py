import requests
import sys
import os
from dotenv import load_dotenv
from functools import lru_cache
from os.path import join, dirname


BASE_URL = f"https://api.spotify.com/v1"


# TODO: Invalidate cache based on token validity
@lru_cache
def _fetch_access_token():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    assert CLIENT_ID and CLIENT_SECRET, "Dotenv config not properly laoded."

    print("Fetching access token from net", file=sys.stderr)
    res = requests.post(
        "https://accounts.spotify.com/api/token", data={
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET
        }, headers={
            "Content-Type": "application/x-www-form-urlencoded"
        })
    # TODO: Error handling
    assert res.status_code == 200, "Error fetching access token"
    return res.json()


@lru_cache
def get_access_token():
    token_response = _fetch_access_token()
    return token_response["access_token"]


@lru_cache
def fetch_artist(artist_id: str, access_token: str) -> object:
    print(f"Fetching artist {artist_id}")
    endpoint = f"/artists/{artist_id}"
    r = requests.get(BASE_URL + endpoint, headers={
        "Authorization": f"Bearer {access_token}"
    })
    # TODO: Error handling
    assert r.status_code == 200, f"Error fetching artist {artist_id} -> status {r}"

    return r.json()


if __name__ == "__main__":
    access_token = get_access_token()
    print(access_token)
    # NOTE: Should only cause 1 access token fetch due to LRU cache
    access_token = get_access_token()
    print(access_token)
    access_token = get_access_token()
    print(access_token)
    access_token = get_access_token()
    test_artist = "4Z8W4fKeB5YxbusRsdQVPb"
    res = fetch_artist(test_artist, access_token)
    print(res)
    res = fetch_artist(test_artist, access_token)
    print(res)
