import gdax
import requests

EXCHANGES = ["GDAX", "BINANCE"]
GDAX_PRODUCTS = ["ETH-BTC", "BCH-BTC", "LTC-BTC"]


def get_exchange_prices(exchange, params=None):
    if exchange not in EXCHANGES:
        return None
    if exchange == "GDAX":
        return get_GDAX_prices()
    elif exchange == "BINANCE":
        return get_BINANCE_prices()


def get_GDAX_prices(params=None):
    public_client = gdax.PublicClient()
    order_book = [public_client.get_product_order_book(
        x) for x in GDAX_PRODUCTS]

    return order_book


def get_BINANCE_prices(params=None):
    pass
