import json
import sys
from typing import List
from fetchers import fetch_my_playlists, fetch_tracks_by_url

# TODO: Typing of playlists
type Track = any
type Playlist = any


def get_unique_tracks(all_tracks) -> List[Track]:
    # TODO: Refactor
    s = set()
    unknown_name = []
    x, y = 0, 0
    for track in all_tracks:
        # print(json.dumps(track, indent=4))
        # return
        # print(track["track"])
        track_name = None
        if "track" in track.keys():
            x += 1
            # print(track["track"])
            if (track["track"]):
                # print(track["track"].keys())
                track_name = track["track"]["name"]
            else:
                print(track)
                y += 1

        if track_name:
            # print("Found track:", track_name)
            pass
        else:
            # TODO: Fix name extraction bug
            unknown_name.append(track)
        # print(track.keys())
        # print(track["track"])
        # print(track["track"].keys())
        # print(track["track"]["name"])
        # exit(1)
        s.add(track_name)
    print("Totalt", len(unknown_name), "tracks uten name", file=sys.stderr)
    print(x, y)
    return list(s)


def print_playlist_names(playlists):
    all_tracks = []
    for playlist in playlists:
        # print(playlist)
        # print(playlist["name"])

        # print("URL for å fetche tracks:", playlist["tracks"])

        fetched_tracks = fetch_tracks_by_url(playlist["tracks"]["href"])
        # print(tracks)
        # print("*****")

        for track in fetched_tracks["items"]:
            # print(json.dumps(track, indent=4))
            # if track.get("type", "track") != "track":
            # print("****")
            # print(track["type"])
            # print(track)
            # continue
            all_tracks.append(track)
            # return

    print(all_tracks[0])
    print(type(all_tracks[0]))
    print("Totalt", len(all_tracks), "tracks")
    # print(json.dumps(all_tracks[0], indent=4))
    # print((all_tracks[0]["track"]["name"]))
    print(len(get_unique_tracks(all_tracks)), "unique tracks")


if __name__ == "__main__":
    # my_playlists = fetch_my_playlists(get_all=False)
    my_playlists = fetch_my_playlists(get_all=True)

    # print(json.dumps(my_playlists, indent=4))
    # print(my_playlists)

    print_playlist_names(my_playlists)
    print("Totalt", len(my_playlists), "playlists")
