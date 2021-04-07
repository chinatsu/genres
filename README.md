# genres

A script that collects listening history for a given [last.fm](https://last.fm) user and uses Spotify to determine genres for the artists, then spits out a chart.

I use [poetry](https://python-poetry.org/) for package management, and I recommended installing this to avoid dealing with virtualenvs on your own.


## Setup

You will need an API application on both [last.fm](https://www.last.fm/api) and [Spotify](https://developer.spotify.com/dashboard/applications).
The application reads (and expects) these environment variables:

|Name|Value|
|--|--|
| SPOTIPY_CLIENT_ID | The Client ID of your Spotify API application |
| SPOTIPY_CLIENT_SECRET | The Client Secret of your Spotify API application |
| SPOTIPY_REDIRECT_URI | A redirect URI that has been registered with your Spotify API application |
| LAST_FM_KEY | The API key from your [Last.fm API application](https://www.last.fm/api/accounts) |
| LAST_FM_SECRET | The API secret from your Last.fm API application |


## Usage

```
usage: python genres [-h] [--days DAYS] [--from START] [--to END] [--top TOP] user

positional arguments:
  user          last.fm user

optional arguments:
  -h, --help    show this help message and exit
  --days DAYS   the amount of days to consider (default: 7)
  --from START  start of the window, YYYY-MM-DD format
  --to END      end of the window, YYYY-MM-DD format
  --top TOP     display the top n genres (default: 20)
```

e.g.

```
poetry run genres toast-rock
```

should spit out something like
```
$ poetry run python genres toast-rock
Processing track number: 300
Processed artists
Processed genres
Saved to charts/toast-rock_2021-03-31-2021-04-07.png
```
