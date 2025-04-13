import requests
import sys
from functools import lru_cache

from config import get_api_client
from user_token import get_user_token


BASE_URL = f"https://api.spotify.com/v1"


# TODO: Invalidate cache based on token validity
@lru_cache
def _fetch_access_token():
    CLIENT_ID, CLIENT_SECRET = get_api_client()
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
    assert res.ok, "Error fetching access token"
    return res.json()


@lru_cache
def get_access_token():
    token_response = _fetch_access_token()
    return token_response["access_token"]


@lru_cache
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


@lru_cache
def fetch_my_playlists() -> object:
    access_token = get_user_token()
    endpoint = "/me/playlists"
    r = requests.get(BASE_URL + endpoint, headers={
        "Authorization": f"Bearer {access_token}"
    })

    # TODO: Error handling
    assert r.ok, f"Error fetching my playlists -> status {r}, {r.json()["error"]["message"]} (you may need to reauthenticate in the browser)"

    print(f"*** Fetched playlists ***", file=sys.stderr)

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
