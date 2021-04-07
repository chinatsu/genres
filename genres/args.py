from argparse import ArgumentParser
from datetime import datetime, timedelta


class Args:
    def __init__(self):
        self.args = Args.parse()
        self.user = self.args.user
        self.top = self.args.top
        self.end = "Bottom" if self.args.top < 0 else "Top"
        self.reverse = False if self.args.top < 0 else True
        self.time_from = (
            int(datetime.strptime(self.args.start, "%Y-%m-%d").timestamp())
            if self.args.start
            else int((datetime.now() - timedelta(days=self.args.days)).timestamp())
        )
        self.time_to = (
            int(datetime.strptime(self.args.start, "%Y-%m-%d").timestamp())
            if self.args.end
            else int(datetime.now().timestamp())
        )
        self.formatted = {
            "from": datetime.fromtimestamp(self.time_from).strftime("%Y-%m-%d"),
            "to": datetime.fromtimestamp(self.time_to).strftime("%Y-%m-%d"),
        }
        if self.time_from > self.time_to:
            raise Exception("--to cannot be smaller than --from")

    @staticmethod
    def parse():
        parser = ArgumentParser(
            "Display the top Spotify genres in the listening history of a given last.fm user"
        )
        parser.add_argument("user", help="last.fm user")
        parser.add_argument(
            "--days",
            help="the amount of days to consider (default: 7)",
            type=int,
            default=7,
        )
        parser.add_argument(
            "--from",
            help="start of the window, YYYY-MM-DD format",
            type=str,
            dest="start",
        )
        parser.add_argument(
            "--to", help="end of the window, YYYY-MM-DD format", type=str, dest="end"
        )
        parser.add_argument(
            "--top", help="display the top n genres (default: 20)", type=int, default=20
        )
        return parser.parse_args()
