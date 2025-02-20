import requests

# Example: Fetch Bitcoin price from Binance API
BINANCE_URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

def get_price():
    response = requests.get(BINANCE_URL)
    data = response.json()
    return float(data["price"])

# Simple trading logic: Buy if price drops below a certain value
BUY_THRESHOLD = 40000  # Change this based on your strategy

def trading_bot():
    price = get_price()
    print(f"Current BTC Price: ${price}")

    if price < BUY_THRESHOLD:
        print("Buying Bitcoin!")  # Replace this with actual buy order logic
    else:
        print("No trade action taken.")

# Run the bot
trading_bot()
