# nostalgeez

Given a Spotify track, when was it added to your playlists?

## Dependencies

- Python3
  - requests
  - certifi
  - dotenv

## Plan

### Sub-problemer

- [x] Må deale med API-keys
- [ ] Finne track id (nødvendig? Kan bruke navn istedet??)
- [ ] Finne alle playlists
- [ ] Finne hvilke playlists som inneholder tracken
- [ ] Finne når sangen ble lagt til i gven playlists
- [ ] Presentere resultatene til brukeren

### Tech

- Node for å interface mot APIet?
- Python for å prosessere API-dataen clientside?
- Begynne med å bare printe resultatene til CLI?
- Se på å bruke Redis for å lagre playlistesene? (obv overkill men kanskje kewl)
- Se på å bruke mySQL for å optimalisere network IO? (-> caching på disk)

### Nice to haves

- Containerisation (for å vise skills mtp portofolio)
- Saklig måte å håndtere API-keys
