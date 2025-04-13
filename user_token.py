
USER_TOKEN_FILE_NAME = "user_token.txt"


def set_user_token(response):
    print("Writing user token to file", USER_TOKEN_FILE_NAME)
    user_token = response["access_token"]
    with open(USER_TOKEN_FILE_NAME, "w") as f:
        f.write(user_token)


def get_user_token():
    # TODO: Should assert user has auth with valid token
    with open(USER_TOKEN_FILE_NAME, "r") as f:
        return f.read()
