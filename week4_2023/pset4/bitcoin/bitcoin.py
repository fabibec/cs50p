import requests
import sys

# Check for missing command-line argument
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    # Check for corecct input value
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

# Request current bitcoin price
api_data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
try:
    bitcoin_price = float(api_data["bpi"]["USD"]["rate"].replace(",",""))
except requests.RequestException:
    sys.exit("Bitcoin price data is not acessible")

# Print the correct amount
price = bitcoin_price * amount
print(f"${price:,}")



