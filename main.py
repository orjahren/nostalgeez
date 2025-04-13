from playlists import get_playlists_by_track_id


modes = [("By date", "Provide a date and get what songs you added on that date", lambda: by_date()),
         ("By ID", "Given a track ID, find when you added it to what lists", lambda: by_id()),
         ("Exit", "", lambda: None)]


def print_menu():
    for i, (name, desc, _) in enumerate(modes):
        print(f"({i + 1}) {name} {desc and f"- {desc}"}")


def main():
    print("*** Nostalgeez ***")

    mode = None
    while mode != len(modes):
        print_menu()
        # TODO: Dont crash on wrong format
        mode = int(input("> "))
        modes[mode-1][2]()


def by_date() -> None:
    print("Will do by date")

    date = input("On what date? Use format YYYY-MM-DD")
    print("OK, date", date)
    pass


def by_id() -> None:
    print("Will do by id")

    test_track_id = "4KuUMa7zmUzVWrDyzf2eaL"

    # track_id = input("What track id?")
    track_id = test_track_id
    print("OK, track id", track_id)

    playlists = get_playlists_by_track_id(track_id)
    print("Res:", len(playlists), "playlists")

    for i, (playlist, added_at) in enumerate(playlists):
        print(f"[{i}] {playlist["name"]} -> {added_at}")

    pass


if __name__ == "__main__":
    # main()
    by_id()
