import json
import sys
from typing import List, Optional

from joblib import Memory
from fetchers import fetch_my_playlists, fetch_tracks_by_url

memory = Memory("/tmp/nostalgeez-cache", verbose=0)

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


@memory.cache
def playlist_contains_track(playlist, track_id) -> Optional[Track]:
    # print(playlist)

    tracks = fetch_tracks_by_url(playlist["tracks"]["href"])
    # print(tracks)
    for track in tracks["items"]:
        # print(track)
        if track["track"]:
            if track["track"]["id"] == track_id:
                return track
    return None


@memory.cache
def get_playlists_by_track_id(track_id: str) -> List[Track]:
    my_playlists = fetch_my_playlists()
    res = []
    for playlist in my_playlists:
        if (track := playlist_contains_track(playlist, track_id)):
            # print(track)
            # print(track["added_at"])
            res.append((playlist, track["added_at"]))

    return res


if __name__ == "__main__":
    # my_playlists = fetch_my_playlists(get_all=False)
    my_playlists = fetch_my_playlists(get_all=True)

    # print(json.dumps(my_playlists, indent=4))
    # print(my_playlists)

    print_playlist_names(my_playlists)
    print("Totalt", len(my_playlists), "playlists")
