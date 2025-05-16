from app.data_fetcher import get_spot_price_and_volatility
from app.utils import time_to_expiry
from app.pricing import black_scholes_price, binomial_price, monte_carlo_barrier, monte_carlo_asian
from app.plot_helpers import plot_price_vs_strike, plot_price_vs_volatility
import matplotlib.pyplot as plt

def main():
    print("=== Options Pricing Engine (CLI) ===")

    ticker = input("Enter stock ticker (e.g. AAPL): ").strip()
    strike = float(input("Enter strike price: "))
    expiry = input("Enter expiry date (YYYY-MM-DD): ").strip()
    r = float(input("Enter risk-free rate (e.g. 0.06): "))
    option_style = input("Option style (European/American/Barrier/Asian): ").strip().capitalize()
    option_type = input("Option type (call/put): ").strip().lower()

    try:
        S, sigma = get_spot_price_and_volatility(ticker)
        T = time_to_expiry(expiry)

        if option_style == "European":
            price = black_scholes_price(S, strike, T, r, sigma, option_type)
        elif option_style == "American":
            price = binomial_price(S, strike, T, r, sigma, option_type, steps=100, american=True)
        elif option_style == "Barrier":
            barrier_type = input("Barrier type (up-and-in/up-and-out/down-and-in/down-and-out): ").strip().lower()
            barrier_level = float(input("Barrier level: "))
            price = monte_carlo_barrier(S, strike, T, r, sigma, option_type, barrier_type, barrier_level, simulations=10000)
        elif option_style == "Asian":
            price = monte_carlo_asian(S, strike, T, r, sigma, option_type, simulations=10000)
        else:
            raise ValueError("Invalid option style.")

        print(f"\nSpot Price: ${S:.2f}")
        print(f"Volatility (1Y): {sigma*100:.2f}%")
        print(f"Time to Expiry: {T*365:.0f} days")
        print(f"{option_style} {option_type.capitalize()} Option Price: ${price:.2f}")

        # --- Visualization Option ---
        print("\nAvailable Visualizations:")
        print("1. Option Price vs Strike Price")
        print("2. Option Price vs Volatility")
        viz_choice = input("Enter choice (1/2 or skip): ").strip()

        if viz_choice == "1":
            fig = plot_price_vs_strike(S, T, r, sigma, option_type)
            plt.show()
        elif viz_choice == "2":
            fig = plot_price_vs_volatility(S, strike, T, r, option_type)
            plt.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
