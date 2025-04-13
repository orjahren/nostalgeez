# nostalgeez

Given a Spotify track, when was it added to your playlists?

## Functionality

- Given a track, find when it was added to which of your playlists
- Given a date, find what songs you added to which playlists accross years

## Usage

TODO: Write usage documentation

## Dependencies

- Python3
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

## TODOs

- [x] Må deale med API-keys
- [ ] Finne track id (nødvendig? Kan bruke navn istedet??)
- [x] Finne alle playlists
- [x] Finne hvilke playlists som inneholder tracken
- [x] Finne når sangen ble lagt til i gven playlists
- [x] Presentere resultatene til brukeren
- [ ] La brukeren gi en dato
- [x] Finne alle playlists som fikk en ny track den datoen
- [ ] Add some optional slack for date check
- [ ] Unit testing?
- [ ] Read arguments from CLI insted of input loop?
- [ ] Should add an auth check early in the pipeline.
- [ ] Må ta høyde for hvem som addet sangen? Hva skjer hvis man følger en playlist og får at man liksom addet noe selv når noen andre gjorde det?

## Further work

The provided code will fetch all your playlists and their songs. You can use this as a base for all sorts of analysis outside of what i have done.

Feel free to fork the project.
