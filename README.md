# nostalgeez

Given a Spotify track, when was it added to your playlists?

## Functionality

- Given a track, find when it was added to which of your playlists
- Given a date, find what songs you added to which playlists accross years

## Dependencies

- Python3
  - requests (API operations)
  - certifi (API operations)
  - dotenv (handle API client secrets)
  - flask (basic webserver for auth)
  - requests_oauthlib (auth)
  - joblib (caching)
- Spotiy API application
  - Claim: Web API
  - Callback URL must match whatever is in [web_client.py](./web_client.py)
    - Or get a user token some other way and write it to the path specified in [user_token.py](./user_token.py)

### Dotenv setup

```
CLIENT_ID=<your client id>
CLIENT_SECRET=<your client secret>
```

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
- [ ] Code cleanup and refactors
