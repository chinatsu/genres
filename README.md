# genres

A script that collects listening history for a given [last.fm](https://last.fm) user and uses Spotify to determine genres for the artists, then spits out a chart.

I use [poetry](https://python-poetry.org/) for package management, and I recommended installing this to avoid dealing with virtualenvs on your own.


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
