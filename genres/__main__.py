from collections import Counter
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

try:
    import secret  # this is where i initialize env variables 'cause i'm lazy & on windows
except:
    pass
from args import Args
import chart
import lastfm


def get_artists(user, args):
    scrobbles = user.get_recent_tracks(
        limit=None, time_from=args.time_from, time_to=args.time_to, stream=True
    )

    print(f"Getting scrobbled artists for {user} in the period {args.formatted['from']} to {args.formatted['to']}")

    artists = []
    for idx, scrobble in enumerate(scrobbles):
        print(f"Processing scrobble number: {idx+1:<7}\r", end="")
        artists.append(scrobble.track.artist.name)
    print()
    if len(artists) == 0:
        raise Exception(
            f"No scrobbles have been registered between {args.formatted['from']} and {args.formatted['to']}"
        )

    counter = Counter(artists)
    print(f"Received {len(counter)} unique artists over {len(artists)} scrobbles")

    return counter


def get_genres(artists, args):
    spotify = Spotify(auth_manager=SpotifyOAuth())
    genres = []
    print()
    print(f"Getting Spotify genres for {len(artists)} artists")
    for idx, artist in enumerate(artists):
        print(f"Processing artist number: {idx+1:<7}\r", end="")
        results = spotify.search(q=f'"{artist}"', type="artist")["artists"][
            "items"
        ]
        if len(results) > 0:
            if results[0]["name"] == artist:
                genres += results[0]["genres"] * artists[artist]

    counter = Counter(genres)
    print()
    print(f"Received {len(counter)} unique genres")

    if args.reverse:
        return [
            item
            for items, c in counter.most_common()[: args.top]
            for item in [items] * c
        ]
    else:
        return [
            item
            for items, c in counter.most_common()[: args.top - 1 : -1]
            for item in [items] * c
        ]


def main():
    args = Args()

    lfm = lastfm.init()
    user = lfm.get_user(args.user)

    artists = get_artists(user, args)
    genres = get_genres(artists, args)
    chart.save(args, genres)


if __name__ == "__main__":
    main()
