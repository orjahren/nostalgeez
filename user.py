import json
import requests

from user_token import get_user_token


if __name__ == "__main__":
    user_token = get_user_token()
    print("Bruker user_token: ", user_token)
    r = requests.get("https://api.spotify.com/v1/me",
                     headers={"Authorization": 'Bearer ' + user_token})

    user = r.json()

    print(json.dumps(user, indent=4))
