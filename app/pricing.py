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
