# nostalgeez

Given a Spotify track, when was it added to your playlists?

## Dependencies

- Python3
  - requests
  - certifi
  - dotenv
  - flask
  - requests_oauthlib
  - joblib
- Spotiy API application
  - Claim: Web API
  - Callback URL must match whatever is in [web_client.py](./web_client.py)
    - Or get a user token some other way and write it to the path specified in [user_token.py](./user_token.py)

### Dotenv setup

```
CLIENT_ID=<your client id>
CLIENT_SECRET=<your client secret>
```

## Plan

### Sub-problemer

- [x] Må deale med API-keys
- [ ] Finne track id (nødvendig? Kan bruke navn istedet??)
- [x] Finne alle playlists
- [x] Finne hvilke playlists som inneholder tracken
- [x] Finne når sangen ble lagt til i gven playlists
- [x] Presentere resultatene til brukeren
- [ ] La brukeren gi en dato
- [x] Finne alle playlists som fikk en ny track den datoen

### Nice to haves

- Containerisation (for å vise skills mtp portofolio)
- Saklig måte å håndtere API-keys
