# main.py

from app.data_fetcher import get_spot_price_and_volatility
from app.utils import time_to_expiry
from app.pricing import black_scholes_price

def main():
    print("=== European Options Pricing Engine (CLI) ===")

    ticker = input("Enter stock ticker (e.g. AAPL): ").strip()
    strike = float(input("Enter strike price: "))
    expiry = input("Enter expiry date (YYYY-MM-DD): ").strip()
    r = float(input("Enter risk-free rate (e.g. 0.06): "))
    option_type = input("Option type (call/put): ").strip().lower()

    try:
        S, sigma = get_spot_price_and_volatility(ticker)
        T = time_to_expiry(expiry)
        price = black_scholes_price(S, strike, T, r, sigma, option_type)

        print(f"\nSpot Price: ${S:.2f}")
        print(f"Volatility (1Y): {sigma*100:.2f}%")
        print(f"Time to Expiry: {T*365:.0f} days")
        print(f"{option_type.capitalize()} Option Price: ${price:.2f}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
