import json
from fetchers import fetch_my_playlists

# TODO: Typing of playlists


def print_playlist_names(playlists):
    for playlist in playlists["items"]:
        # print(playlist)
        print(playlist["name"])


if __name__ == "__main__":
    my_playlists = fetch_my_playlists()

    # print(json.dumps(my_playlists, indent=4))
    # print(my_playlists)

    print_playlist_names(my_playlists)
