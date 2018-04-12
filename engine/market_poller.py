# coding=utf-8
import ccxt
import time
import pprint

delay = 2  # seconds

pp = pprint.PrettyPrinter(indent=2)

binance = ccxt.binance()
binance_markets = binance.load_markets()

gdax = ccxt.gdax()
gdax_markets = gdax.load_markets()

# pp.pprint(gdax.fetch_order_book("ETH/BTC"))
# pp.pprint(binance.fetch_order_book("ETH/BTC"))
while True:

    gdax_order_book = gdax.fetch_order_book("ETH/BTC")
    binance_order_book = binance.fetch_order_book("ETH/BTC")

    gdax_sell_price = gdax_order_book['bids'][0][0]
    gdax_buy_price = gdax_order_book['asks'][0][0]

    binance_sell_price = binance_order_book['bids'][0][0]
    binance_buy_price = binance_order_book['asks'][0][0]

    print(binance_sell_price)
    print(binance_buy_price)

    print("Profit to sell ETH on gdax, buy on binance: Price Difference {}, Percent: {}".format(
        binance_buy_price-gdax_sell_price, ((binance_buy_price-gdax_sell_price)/float(gdax_sell_price)) * 100))
    print("Profit to sell ETH on binance, buy on gdax: Price Difference: {}, Percent: {}".format(
        gdax_buy_price - binance_sell_price, ((gdax_buy_price - binance_sell_price)/float(binance_sell_price)) * 100))
    print("--------------------------------")

    time.sleep(2)
