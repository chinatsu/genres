from collections import Counter
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime

try:
    import secret  # this is where i initialize env variables 'cause i'm lazy & on windows
except:
    pass
from args import Args
import chart
import lastfm


def get_scrobbles(user, args):
    scrobbles = user.get_recent_tracks(
        limit=None, time_from=args.time_from, time_to=args.time_to, stream=True
    )

    details = []
    artists = []
    for idx, scrobble in enumerate(scrobbles):
        if idx % 100 == 0 and idx != 0:
            print(f"Processing scrobble number: {idx}         \r", end="")
        artist = scrobble.track.artist.name
        artists.append(artist)
        details.append(
            {
                "artist": artist,
                "date": datetime.fromtimestamp(int(scrobble.timestamp)),
                "genres": [],
            }
        )
    print()
    if len(artists) == 0:
        raise Exception(
            f"No scrobbles have been registered between {args.formatted['from']} and {args.formatted['to']}"
        )

    print(f"Processed {len(details)} scrobbles")

    return set(artists), details


def get_genres(artists, args):
    spotify = Spotify(auth_manager=SpotifyOAuth())
    genres = {}
    for idx, artist in enumerate(artists):
        if idx % 100 == 0 and idx != 0:
            print(f"Processing artist number: {idx}         \r", end="")
        results = spotify.search(q=f"artist:{artist}", type="artist")["artists"][
            "items"
        ]
        if len(results) > 0:
            genres[artist] = results[0]["genres"]

    print()
    print(f"Received genres for {len(genres)} artists")

    return genres


def produce_history(scrobbles, genres):
    history = []
    for scrobble in scrobbles:
        if scrobble["artist"] in genres:
            for genre in genres[scrobble["artist"]]:
                history.append({"genre": genre, "date": scrobble["date"]})
    return list(reversed(history))


def main():
    args = Args()

    lfm = lastfm.init()
    user = lfm.get_user(args.user)

    artists, scrobbles = get_scrobbles(user, args)
    genres = get_genres(artists, args)
    history = produce_history(scrobbles, genres)
    chart.save(args, history, genres)


if __name__ == "__main__":
    main()
