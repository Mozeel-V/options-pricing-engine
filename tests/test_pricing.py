# tests/test_pricing.py

import pytest
from app.pricing import black_scholes_price

def test_call_option_price():
    # Known example values
    S = 100      # Spot price
    K = 100      # Strike price
    T = 1        # Time to expiry in years
    r = 0.05     # Risk-free rate (5%)
    sigma = 0.2  # Volatility (20%)
    option_type = "call"

    price = black_scholes_price(S, K, T, r, sigma, option_type)

    # Approx expected value from textbook
    assert round(price, 2) == 10.45

def test_put_option_price():
    S = 100
    K = 100
    T = 1
    r = 0.05
    sigma = 0.2
    option_type = "put"

    price = black_scholes_price(S, K, T, r, sigma, option_type)
    
    assert round(price, 2) == 5.57
