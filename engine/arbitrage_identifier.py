import endpoint_wrapper


class ArbitrageIdentifier:
    # order_book = {exchange_name: crypto_name: {bid: named_tuple(bid_price, bid_quantity), ask: named_tuple(ask_price, ask_quantity)}}
    def __init__(self, config=None):
        self.exchanges = config["exchanges"]
        #self.constraints = config["constraints"]
        #self.cryptos = config["cryptos"]
        self.order_book = {}

    # Populate the order book with prices from all exchanges
    def get_market_data(self):
        for exchange in self.exchanges:
            prices = endpoint_wrapper.get_exchange_prices(exchange)
            print("Prices for Exchange: {}".format(exchange))
            print(prices)

    # Identify arbitrage opportunities within a single exchange, subject to constraints
    def identify_single_market_arbitrage(self):
        pass

    # Identify arbitrage opportunities across exchanges, subject to constraints
    def identify_multi_market_arbitrage(self):
        pass


x = ArbitrageIdentifier(config={"exchanges": ["GDAX"]})
x.get_market_data()
