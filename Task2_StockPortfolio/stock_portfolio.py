# CodeAlpha Internship - Task 2
# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}

portfolio = []
total_investment = 0

print("=" * 40)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 40)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Invalid stock symbol. Please choose from the available stocks.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    price = stock_prices[stock_name]
    investment = price * quantity

    portfolio.append((stock_name, quantity, price, investment))
    total_investment += investment

    print(f"Added {quantity} share(s) of {stock_name}.")
    print(f"Investment value: ${investment}")

print("\n" + "=" * 40)
print("           PORTFOLIO SUMMARY")
print("=" * 40)

if portfolio:
    for stock, quantity, price, investment in portfolio:
        print(
            f"{stock}: {quantity} share(s) × ${price} = ${investment}"
        )

    print("-" * 40)
    print(f"Total Investment: ${total_investment}")
else:
    print("No stocks were added.")

print("=" * 40)
print("Thank you for using the Stock Portfolio Tracker!")
