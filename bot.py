# bot.py
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)

        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com"

        logging.info("Trading bot initialized (Testnet=%s)", testnet)

    # -----------------------------------------
    # Place Market Order
    # -----------------------------------------
    def place_market_order(self, symbol, side, quantity):
        try:
            logging.info(f"Placing MARKET order: {symbol}, Side={side}, Qty={quantity}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="MARKET",
                quantity=quantity
            )

            logging.info(f"Order Placed: {order}")
            return order

        except Exception as e:
            logging.error(f"Market order failed: {str(e)}")
            return None

    # -----------------------------------------
    # Place Limit Order
    # -----------------------------------------
    def place_limit_order(self, symbol, side, quantity, price):
        try:
            logging.info(f"Placing LIMIT order: {symbol}, Side={side}, Qty={quantity}, Price={price}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="LIMIT",
                price=price,
                timeInForce="GTC",
                quantity=quantity
            )

            logging.info(f"Order Placed: {order}")
            return order

        except Exception as e:
            logging.error(f"Limit order failed: {str(e)}")
            return None

    # -----------------------------------------
    # BONUS — Stop-Limit Order
    # -----------------------------------------
    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            logging.info(f"Placing STOP-LIMIT: Stop={stop_price}, Limit={limit_price}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="STOP",
                stopPrice=stop_price,
                price=limit_price,
                timeInForce="GTC",
                quantity=quantity
            )

            logging.info(f"Stop-Limit Order: {order}")
            return order

        except Exception as e:
            logging.error(f"Stop-Limit failed: {str(e)}")
            return None
