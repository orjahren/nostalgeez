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

## Plan

### Sub-problemer

- [x] Må deale med API-keys
- [ ] Finne track id (nødvendig? Kan bruke navn istedet??)
- [x] Finne alle playlists
- [x] Finne hvilke playlists som inneholder tracken
- [x] Finne når sangen ble lagt til i gven playlists
- [x] Presentere resultatene til brukeren
- [ ] La brukeren gi en dato
- [ ] Finne alle playlists som fikk en ny track den datoen

### Tech

- Node for å interface mot APIet?
- Python for å prosessere API-dataen clientside?
- Begynne med å bare printe resultatene til CLI?
- Se på å bruke Redis for å lagre playlistesene? (obv overkill men kanskje kewl)
- Se på å bruke mySQL for å optimalisere network IO? (-> caching på disk)

### Nice to haves

- Containerisation (for å vise skills mtp portofolio)
- Saklig måte å håndtere API-keys
