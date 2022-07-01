import os

from dotenv import load_dotenv
from lemon import api

load_dotenv()
client = api.create(
    market_data_api_token=os.getenv("DATA_API_KEY"),
    trading_api_token=os.getenv("TRADING_API_KEY"),
    env="paper"
)


def get_venues():
    response = client.market_data.venues.get()
    print(response)


def get_instruments():
    response = client.market_data.instruments.get()
    print(response)


def get_quotes():
    response = client.market_data.quotes.get_latest(isin="US19260Q1076")
    print(response)


def get_ohlc():
    response = client.market_data.ohlc.get(isin="DE0008404005", period="d1")
    print(response)


def get_trades():
    response = client.market_data.trades.get_latest(isin="DE0008404005")
    print(response)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_trades()
    get_instruments()
    get_quotes()
    get_ohlc()
    get_trades()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
