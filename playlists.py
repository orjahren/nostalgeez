import json
from fetchers import fetch_my_playlists, fetch_tracks_by_url

# TODO: Typing of playlists


def print_playlist_names(playlists):
    for playlist in playlists:
        # print(playlist)
        print(playlist["name"])

        print("URL for å fetche tracks:", playlist["tracks"])

        tracks = fetch_tracks_by_url(playlist["tracks"]["href"])
        print(tracks)
        print("*****")

        for track in tracks["items"]:
            print(json.dumps(track, indent=4))
            return


if __name__ == "__main__":
    # my_playlists = fetch_my_playlists(get_all=False)
    my_playlists = fetch_my_playlists(get_all=True)

    # print(json.dumps(my_playlists, indent=4))
    # print(my_playlists)

    print("Totalt", len(my_playlists), "playlists")

    # print_playlist_names(my_playlists)
