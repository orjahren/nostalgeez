import os
from posixpath import dirname, join
from dotenv import load_dotenv


def get_api_client():
    dotenv_path = join(dirname(__file__), '.env')
    print(dotenv_path)
    load_dotenv(dotenv_path)
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

    print(CLIENT_ID, CLIENT_SECRET)
    return CLIENT_ID, CLIENT_SECRET


if __name__ == "__main__":
    print(get_api_client())
