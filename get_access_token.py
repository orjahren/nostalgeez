import subprocess
import json
from functools import lru_cache
import sys


# TODO: Invalidate cache based on token validity
@lru_cache
def get_access_token():
    print("Fetching access token from net", file=sys.stderr)
    res = subprocess.run(["sh", "get_access_token.sh"], stdout=subprocess.PIPE)
    parsed = json.loads(res.stdout.decode("utf-8"))
    # TODO: Error handling
    return parsed["access_token"]


if __name__ == "__main__":
    access_token = get_access_token()
    print(access_token)
    # NOTE: Should only cause 1 network IO due to LRU cache
    access_token = get_access_token()
    print(access_token)
    access_token = get_access_token()
    print(access_token)
