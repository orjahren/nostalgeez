import json
from fetchers import fetch_artist


# TODO: Typing for artist
def format_artist_info(artist: object) -> str:
    return f"<Artist {artist["name"]} has {artist["followers"]["total"]} followers and these genres: {artist["genres"]}>"


if __name__ == "__main__":
    artists = {"radiohead": "4Z8W4fKeB5YxbusRsdQVPb"}

    for name, _id in artists.items():
        print("Fetching", name)
        artist = fetch_artist(_id)

        print(json.dumps(artist, indent=4))

        print(format_artist_info(artist))
