

import json
import requests

from user_token import get_user_token


if __name__ == "__main__":
    access_token = get_user_token()
    print("Bruker access_token: ", access_token)
    r = requests.get("https://api.spotify.com/v1/me",
                     headers={"Authorization": 'Bearer ' + access_token})

    user = r.json()

    print(json.dumps(user, indent=4))
