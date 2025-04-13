

import requests

from fetchers import get_access_token
from user_token import get_user_token

# import web_client

if __name__ == "__main__":
    import web_client
    user = None
    access_token = get_user_token()
    print("Bruker access_token: ", access_token)
    r = requests.get("https://api.spotify.com/v1/me", headers={
        "Authorization": 'Bearer ' + access_token
    }
    )

    user = r.json()

    print(user)
