modes = [("By date", "Provide a date and get what songs you added on that date"),
         ("By ID", "Given a track ID, find when you added it to what lists"),
         ("Exit", "")]


def print_menu():
    for i, (name, desc) in enumerate(modes):
        print(f"({i + 1}) {name} {desc and f"- {desc}"}")


def main():
    print("*** Nostalgeez ***")

    mode = None
    while mode != len(modes):
        print_menu()
        # TODO: Dont crash on wrong format
        mode = int(input("> "))

        match mode:
            case 1:
                by_date()
            case 2:
                by_id()
            case 3:
                pass


def by_date(date: str) -> None:
    print("Will do by date")
    pass


def by_id() -> None:
    print("Will do by id")
    pass


if __name__ == "__main__":
    main()
