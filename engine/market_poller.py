import endpoint_wrapper


class MarketPoller:
    # order_book = {exchange_name: crypto_name: {bid: named_tuple(bid_price, bid_quantity), ask: named_tuple(ask_price, ask_quantity)}}
    def __init__(self, config=None):
        self.exchanges = config["exchanges"]
        self.order_book = {}

    # Populate the order book with prices from all exchanges
    def get_market_data(self):
        for exchange in self.exchanges:
            prices = endpoint_wrapper.get_exchange_prices(exchange)
            print("Prices for Exchange: {}".format(exchange))
            print(prices)


x = MarketPoller(config={"exchanges": ["GDAX"]})
x.get_market_data()
