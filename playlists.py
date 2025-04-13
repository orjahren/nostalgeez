from fetchers import fetch_my_playlists


if __name__ == "__main__":
    my_playlists = fetch_my_playlists()

    print(my_playlists)
