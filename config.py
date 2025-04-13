from ntpath import join
import os
from posixpath import dirname
from dotenv import load_dotenv


def get_api_client():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

    return CLIENT_ID, CLIENT_SECRET
