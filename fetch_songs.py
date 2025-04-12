from get_access_token import get_access_token


def fetch_songs(access_token: str):
    print(f"Fetching songs with access token ${access_token}")

    print("*** MOCK: Fetcher sanger")


if __name__ == "__main__":
    print("access token:")
    access_token = get_access_token()
    fetch_songs(access_token)
