import os
from pylast import LastFMNetwork

KEY = "LAST_FM_KEY"
SECRET = "LAST_FM_SECRET"


def init():
    try:
        last_fm_key = os.environ[KEY]
        last_fm_secret = os.environ[SECRET]
    except KeyError as e:
        raise Exception(f"Missing required environment variable {e}")
    return LastFMNetwork(api_key=last_fm_key, api_secret=last_fm_secret)
