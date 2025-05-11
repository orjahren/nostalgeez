# nostalgeez

Given a Spotify track, when was it added to your playlists?

```
$ python main.py
*** Nostalgeez ***
(1) By date - Provide a date and get what songs you added on that date
(2) By ID - Given a track ID, find when you added it to what lists
(3) Exit
> 1
OK, date 2025-05-11 01:00:00

On 11.5, 5 songs were added. They are:
	Dust - feat. Astrid S -> This Is What You Came For (feat. Rihanna) – Calvin Harris (2020-05-11T17:45:39Z)
	Circles -> This Is What You Came For (feat. Rihanna) – Calvin Harris (2020-05-11T12:06:45Z)
	Friends (feat. Bon Iver) -> This Is What You Came For (feat. Rihanna) – Calvin Harris (2020-05-11T06:24:47Z)
	Wojtek 2018 -> rt 2,6M (2018-05-11T19:30:47Z)
	Jumanji 2019 -> rt 2,6M (2018-05-11T19:27:13Z)
```

## Functionality

- Given a track, find when it was added to which of your playlists
- Given a date, find what songs you added to which playlists accross years

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

## Usage

_Assuming the setup described above has been completed_.

### Get user token

First, you need to get a user token. In order to do this, you run `python
web_client.py`. This will start the [Flask server](./web_client.py).

Having done this, open your web browser and go to `localhost:3000`. Click the
`Authenticate` button and sign in with your Spotify credentials and aprove
access.

You will be redirected back to a page showing some JSON. This indicates that you
have succeeded in obtaining a user token. The same JSON that you see on screen
will have been written to a file on disk.

You can now both (1) close the web browser and (2) shut down the Flask server.

Note that it is not nessecarry to get a new user token every time you want to
run the software.

### Running

Being in posession of a valid user token, you can run the program by executing
`python main.py`. You will be presented with a modal selection:

```
$ python main.py
*** Nostalgeez ***
(1) By date - Provide a date and get what songs you added on that date
(2) By ID - Given a track ID, find when you added it to what lists
(3) Exit
>
```

Enter the number corresponding to the action you wish to make.

If it is your first time running the software, it will download your playlists.
This may take some time. If you have previously ran the software, your playlists
will be saved to your disk and there will not be need for downloading them
again.

You can see an example output [above](#nostalgeez).

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
- [ ] Clearify Windows support?
  - [ ] Test on Windows. Might just work.

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
