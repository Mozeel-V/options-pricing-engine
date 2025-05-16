# app/pricing.py -> contains Black-Scholes formulas for European options

import numpy as np
from scipy.stats import norm

def black_scholes_price(S, K, T, r, sigma, option_type="call"):
    """
    Parameters:
    S : Spot price
    K : Strike price
    T : Time to expiry (in years)
    r : Risk-free rate (e.g., 0.06 for 6%)
    sigma : Volatility (annualized)
    option_type : "call" or "put"

    Returns:
    Option price (float)
    """
    if T <= 0 or sigma <= 0:
        return 0.0

    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be either 'call' or 'put'")
    
def binomial_price(S, K, T, r, sigma, option_type, steps=100, american=True):
    """
    Cox-Ross-Rubinstein Binomial Tree pricing for American options.
    S: Spot price
    K: Strike price
    T: Time to expiry (in years)
    r: Risk-free rate
    sigma: Volatility
    option_type: "call" or "put"
    steps: Number of time steps in the tree
    american: If True, price as American option else European
    """
    dt = T / steps
    u = np.exp(sigma * np.sqrt(dt))      # up-factor
    d = 1 / u                           # down-factor
    p = (np.exp(r * dt) - d) / (u - d)  # risk-neutral prob

    # Initialize asset prices at maturity
    asset_prices = np.zeros(steps + 1)
    option_values = np.zeros(steps + 1)

    for i in range(steps + 1):
        asset_prices[i] = S * (u ** (steps - i)) * (d ** i)
        if option_type == "call":
            option_values[i] = max(0, asset_prices[i] - K)
        else:
            option_values[i] = max(0, K - asset_prices[i])

    # Step backwards through tree
    for step in range(steps - 1, -1, -1):
        for i in range(step + 1):
            option_values[i] = (
                np.exp(-r * dt) * (p * option_values[i] + (1 - p) * option_values[i + 1])
            )
            if american:
                asset_price = S * (u ** (step - i)) * (d ** i)
                if option_type == "call":
                    option_values[i] = max(option_values[i], asset_price - K)
                else:
                    option_values[i] = max(option_values[i], K - asset_price)

    return option_values[0]

