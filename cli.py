import argparse

class Parser():
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="dbtrader",
            description="CLI trader built in Python for trading pairs",
            epilog='db-trader backtest --plot --time 365 --start 01012025 --data "data.csv"'
        )

        self.subparsers = self.parser.add_subparsers(
            dest="command",
            required=True
        )

        # Fetcher
        self.fetch = self.subparsers.add_parser(
            name="fetch",
            help="Fetches pair data from API."
        )

        self.fetch.add_argument(
            "--path",
            default="./data",
            help="Full file path where data will be saved."
        )

        self.fetch.add_argument(
            "--pair",
            required=True,
            type=str,
            help="Trade pair in the following style: BTC/USD."
        )

        self.fetch.add_argument(
            "--time",
            required=True,
            type=int,
            help="Amount of days of data should be returned."
        )

        self.fetch.add_argument(
            "--time-frame",
            required=False,
            type=str,
            default="1h",
            help="The time-frame at which the data is retrived."
        )

        self.fetch.add_argument(
            "--start",
            required=False,
            type=int,
            help="The date at which the data should start. Form ddmmyyyy"
        )

        # Backtester
        self.backtest = self.subparsers.add_parser(
            name="backtest",
            help="Run strategy backtest."
        )

        self.backtest.add_argument(
            "--data",
            required=True,
            help="Data of historical prices. CSV file."
        )

        self.backtest.add_argument(
            "--plot",
            action="store_true",
            default=False,
            help="Plot results."
        )

        self.args = vars(self.get_args())

    def get_args(self):
        return self.parser.parse_args()

    def get_command(self):
        return self.args.command