# bot.py
import logging
from binance.client import Client

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)

        if testnet:
            testnet_url = "https://testnet.binancefuture.com"
            self.client.FUTURES_URL = testnet_url
            self.client.FUTURES_API_URL = testnet_url
            self.client.API_URL = testnet_url

        logging.info("Initialized bot (Testnet Futures)")

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="MARKET",
                quantity=quantity
            )
            logging.info(order)
            return order
        except Exception as e:
            logging.error(f"Market Order Error: {str(e)}")
            print("❌ ERROR:", e)
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="LIMIT",
                price=price,
                quantity=quantity,
                timeInForce="GTC"
            )
            logging.info(order)
            return order
        except Exception as e:
            logging.error(f"Limit Order Error: {str(e)}")
            print("❌ ERROR:", e)
            return None
