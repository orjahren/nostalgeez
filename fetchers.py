import json
import requests
import sys
from joblib import Memory, expires_after

from config import get_api_client
from user_token import get_user_token


memory = Memory("/tmp/nostalgeez-cache", verbose=0)

BASE_URL = f"https://api.spotify.com/v1"


@memory.cache(cache_validation_callback=expires_after(seconds=3600))
def _fetch_access_token():
    CLIENT_ID, CLIENT_SECRET = get_api_client()
    assert CLIENT_ID and CLIENT_SECRET, "Dotenv config not properly loaded."

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
    assert res.ok, "Error fetching access token"
    return res.json()


def get_access_token():
    token_response = _fetch_access_token()
    return token_response["access_token"]


@memory.cache
def fetch_artist(artist_id: str) -> object:
    access_token = get_access_token()
    print(f"Fetching artist {artist_id}", file=sys.stderr)
    endpoint = f"/artists/{artist_id}"
    r = requests.get(BASE_URL + endpoint, headers={
        "Authorization": f"Bearer {access_token}"
    })
    # TODO: Error handling
    assert r.ok, f"Error fetching artist {artist_id} -> status {r}"

    print(f"*** Fetched artist {r.json()["name"]} ***", file=sys.stderr)

    return r.json()


@memory.cache
def fetch_my_playlists(get_all: bool = True) -> object:
    access_token = get_user_token()
    endpoint = "/me/playlists"
    r = requests.get(BASE_URL + endpoint, headers={
        "Authorization": f"Bearer {access_token}"
    })

    # TODO: Error handling
    assert r.ok, f"Error fetching my playlists -> status {r}, {r.json()["error"]["message"]} (you may need to reauthenticate in the browser)"

    # TODO: This should be heavily refactored.
    resp = r.json()

    if not get_all:
        print("Will not fetch all playlists.")
        return resp["items"]

    batches = []
    batches.append(resp["items"])

    while resp["next"]:

        print("*** Fetching", resp["next"])
        r = requests.get(resp["next"], headers={
            "Authorization": f"Bearer {access_token}"
        })
        resp = r.json()
        batches.append(resp["items"])

    print(f"*** Fetched all playlists ***", file=sys.stderr)

    print(json.dumps(resp, indent=4))
    print(r)

    flat_playlists = [
        playlist
        for batch in batches
        for playlist in batch
    ]

    assert len(flat_playlists) == resp["total"], "Bug in flattening playlists."

    return flat_playlists


@memory.cache
def fetch_tracks_by_url(url: str):
    user_token = get_user_token()
    print(f"Fetching tracks for playlist", file=sys.stderr)
    r = requests.get(url, headers={
        "Authorization": f"Bearer {user_token}"
    })
    # TODO: Error handling
    assert r.ok, f"Error fetching tracks -> status {r}"

    # print(r.json())
    print(f"*** Fetched playlist tracks ***", file=sys.stderr)

    return r.json()


@memory.cache
def fetch_track_by_id(track_id: str):
    access_token = get_access_token()
    print(f"Fetching track by id {track_id}", file=sys.stderr)
    url = BASE_URL + "/tracks/" + track_id
    r = requests.get(url, headers={
        "Authorization": f"Bearer {access_token}"
    })
    # TODO: Error handling
    assert r.ok, f"Error fetching track -> status {r}, {r.json()["error"]["message"]}"

    # print(r.json())
    print(f"*** Fetched track ***", file=sys.stderr)

    return r.json()


def fetch_available_play_devices():
    endpoint = "/me/player/devices"
    user_token = get_user_token()

    print(f"Fetching available devices", file=sys.stderr)
    url = BASE_URL + endpoint
    r = requests.get(url, headers={
        "Authorization": f"Bearer {user_token}"
    })
    # TODO: Error handling
    assert r.ok, f"Error fetching devices -> status {r}, {r.json()["error"]["message"]}"

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
    test_artist = "4Z8W4fKeB5YxbusRsdQVPb"  # Radiohead
    res = fetch_artist(test_artist)
    print(res)
    res = fetch_artist(test_artist)
    print(res)
