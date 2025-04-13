
from fetchers import fetch_track_by_id


def get_id_from_name(name: str) -> str:
    # TODO: Impelement.
    # TODO: API has search feature?
    pass


def get_track_name_by_id(track_id: str) -> str:
    track = fetch_track_by_id(track_id)
    # print(track)
    return track["name"]
