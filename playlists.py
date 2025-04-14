import datetime
from dateutil import parser
import json
import sys
from typing import List, Optional

import dateutil.parser
from joblib import Memory
from date import dates_are_same_of_year
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
def get_playlists_by_track_id(track_id: str) -> List[Playlist]:
    my_playlists = fetch_my_playlists()
    res = []
    for playlist in my_playlists:
        if (track := playlist_contains_track(playlist, track_id)):
            # print(track)
            # print(track["added_at"])
            res.append((playlist, track["added_at"]))

    return res


@memory.cache
def tracks_playlist_got_on_date(playlist: Playlist,  date: datetime.date) -> List[Track]:
    # print(playlist)

    tracks = fetch_tracks_by_url(playlist["tracks"]["href"])
    # print(tracks)
    # exit(1)
    res = []
    for track in tracks["items"]:
        parsed_add_date = parser.parse(track["added_at"])
        if dates_are_same_of_year(parsed_add_date, date):
            res.append(track)
    return res


def get_filtered_playlists_by_date(date: datetime.date) -> List[Playlist]:
    my_playlists = fetch_my_playlists()
    res = []
    for playlist in my_playlists:
        for track in tracks_playlist_got_on_date(playlist, date):
            res.append((playlist, track))

    # Sort by added date, most recent first.
    return sorted(res, key=lambda tup: tup[1]["added_at"], reverse=True)


if __name__ == "__main__":
    # my_playlists = fetch_my_playlists(get_all=False)
    my_playlists = fetch_my_playlists(get_all=True)

    # print(json.dumps(my_playlists, indent=4))
    # print(my_playlists)

    print_playlist_names(my_playlists)
    print("Totalt", len(my_playlists), "playlists")
