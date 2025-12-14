# cli.py
import logging
from bot import BasicBot
from config import API_KEY, API_SECRET

logging.basicConfig(
    filename="logs/bot.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

def validate_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("❌ Enter a valid number!")

def validate_side():
    while True:
        side = input("Buy or Sell? ").upper()
        if side in ["BUY", "SELL"]:
            return side
        print("❌ Invalid side. Choose BUY or SELL")

def main():
    print("=== Binance Futures Testnet Trading Bot ===")

    bot = BasicBot(API_KEY, API_SECRET)

    symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()

    print("\nOrder Types:")
    print("1. Market")
    print("2. Limit")
    print("3. Stop-Limit")

    choice = input("Select order type: ")

    side = validate_side()
    qty = validate_float("Enter quantity: ")

    if choice == "1":
        resp = bot.place_market_order(symbol, side, qty)

    elif choice == "2":
        price = validate_float("Enter limit price: ")
        resp = bot.place_limit_order(symbol, side, qty, price)

    elif choice == "3":
        stop = validate_float("Enter stop price: ")
        limit = validate_float("Enter limit price: ")
        resp = bot.place_stop_limit_order(symbol, side, qty, stop, limit)

    else:
        print("❌ Invalid option")
        return

    print("\n--- ORDER RESPONSE ---")
    print(resp)
    print("----------------------")

if __name__ == "__main__":
    main()
