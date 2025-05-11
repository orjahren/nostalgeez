# nostalgeez

Given a Spotify track, when was it added to your playlists?

## Functionality

- Given a track, find when it was added to which of your playlists
- Given a date, find what songs you added to which playlists accross years

## Usage

TODO: Write usage documentation

## Dependencies

- Python3 (`pip install -r requirements.txt`)
  - requests (API operations)
  - certifi (API operations)
  - dotenv (handle API client secrets)
  - flask (basic webserver for auth)
  - requests_oauthlib (auth)
  - joblib (caching)
- Spotify API application
  - Claim: Web API
  - Callback URL must match whatever is in [web_client.py](./web_client.py)
    - Or get a user token some other way and write it to the path specified in [user_token.py](./user_token.py)

### Dotenv setup

You must have a file [./.env](./.env) and it must be like this:

```
CLIENT_ID=<your client id>
CLIENT_SECRET=<your client secret>
```

It is only ever accessed in [config.py](./config.py).

## Known weaknesses / TODOs

### User oriented

- [ ] Should add an auth check early in the pipeline.
  - Check for auth and fail gracefully. There will currently be a hard crash
    upon invalid auth.
- [ ] Allow the user to find track id by song name.
- [ ] Allow the user to input a date.
  - Now it will always assume the current date.
- [ ] Add some optional slack for date check
  - While you add a song on date `n`, you typically listen to it on date `n+k`.
- [ ] Should consider that the song was added by the user. Relevant for
      collaborative playlists.
- [ ] Support for specific seasons.
  - E.g. "these are your most played [easter, summer, xmas] songs"

### Tech oriented

- [ ] Unit testing
- [ ] Read arguments from CLI insted of input loop
- [ ] Deployment
  - Only local running for now.
  - It is cumbersome that the user has to register an API application in order
    to run this for themself.

## Further work

The provided code will fetch all your playlists and their songs. You can use this as a base for all sorts of analysis outside of what i have done.

Feel free to fork the project.
