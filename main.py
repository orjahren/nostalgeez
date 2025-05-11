import datetime
from playlists import get_filtered_playlists_by_date, get_playlists_by_track_id
from tracks import get_track_name_by_id


modes = [("By date", "Provide a date and get what songs you added on that date", lambda: by_date()),
         ("By ID", "Given a track ID, find when you added it to what lists", lambda: by_id()),
         ("Exit", "", lambda: None)]


def print_menu():
    for i, (name, desc, _) in enumerate(modes):
        print(f"({i + 1}) {name} {desc and f"- {desc}"}")

    return True


def menu_loop():
    print("*** Nostalgeez ***")

    # TODO: Dont crash on wrong input format
    while (mode := (int(input("> ")) if (print_menu()) else 0)) < len(modes):
        modes[mode-1][2]()


def by_date() -> None:
    # TODO: Add some optional slack? e.g. 3 days slack
    print("Will do by date")

    test_date = datetime.datetime.now()

    print(test_date)
    # date = input("On what date? Use format DD-MM")
    date = test_date

    # Truncate to 0 to get cache gains
    date = date.replace(
        hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(hours=1)
    print("OK, date", date)

    print("\n\n")

    playlists = get_filtered_playlists_by_date(date)
    print(
        f"On {date.day}.{date.month}, {len(playlists)} songs were added. They are:")
    for playlist, track in playlists:
        print(
            f"\t{track["track"]["name"]} -> {playlist["name"]} ({track["added_at"]})")
    print("\n")


def by_id() -> None:
    print("Will do by id")

    # test_track_id = "4KuUMa7zmUzVWrDyzf2eaL" # King gus 2018

    track_id = input("What track id? >")
    # track_id = test_track_id
    print("OK, track id", track_id)

    track_name = get_track_name_by_id(track_id)

    print("That is", track_name)

    playlists = get_playlists_by_track_id(track_id)
    print("Res:", len(playlists), "playlists")

    for i, (playlist, added_at) in enumerate(playlists):
        print(f"[{i + 1}] {playlist["name"]} -> {added_at}")
    print("\n\n")


def test():
    tracks = ["3UybjBFuoeBzdfKuovcduL",
              "4KuUMa7zmUzVWrDyzf2eaL", "203SOw9ae8G0bDgCeyijz6"]
    for track_id in tracks:
        print("\n********\n")
        print("OK, track id", track_id)

        track_name = get_track_name_by_id(track_id)

        print("That is", track_name)

        playlists = get_playlists_by_track_id(track_id)
        print("Res:", len(playlists), "playlists")

        for i, (playlist, added_at) in enumerate(playlists):
            print(f"[{i}] {playlist["name"]} -> {added_at}")


if __name__ == "__main__":
    # main()
    # by_id()
    # test()
    # by_date()
    menu_loop()
