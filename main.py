from models.MarketData import MarketData


def get_venues():
    endpoint = f'venues/'
    response = MarketData().get_response(endpoint)
    print(response)


def get_instruments():
    endpoint = f'instruments/?search=Tesla&tradable=True&type=stock'
    response = MarketData().get_response(endpoint)
    print(response)


def get_quotes():
    endpoint = f'quotes/?isin=US19260Q1076'
    response = MarketData().get_response(endpoint)
    print(response)


def get_ohlc():
    endpoint = f'ohlc/d1/?isin=DE0008404005'
    response = MarketData().get_response(endpoint)
    print(response)


def get_trades():
    endpoint = f'trades/?isin=US19260Q1076'
    response = MarketData().get_response(endpoint)
    print(response)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_trades()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
