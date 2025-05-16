# tests/test_pricing.py

import pytest
from app.pricing import black_scholes_price, binomial_price

def test_black_scholes_call():
    S = 100    # Spot price
    K = 100    # Strike price
    T = 1.0    # 1 year to expiry
    r = 0.05   # 5% risk-free rate
    sigma = 0.2 # 20% volatility
    option_type = "call"

    price = black_scholes_price(S, K, T, r, sigma, option_type)
    assert price > 0
    assert round(price, 2) == 10.45  # Known value from Black-Scholes calculator

def test_black_scholes_put():
    S = 100
    K = 100
    T = 1.0
    r = 0.05
    sigma = 0.2
    option_type = "put"

    price = black_scholes_price(S, K, T, r, sigma, option_type)
    assert price > 0
    assert round(price, 2) == 5.57

def test_binomial_call_european():
    S = 100
    K = 100
    T = 1.0
    r = 0.05
    sigma = 0.2
    option_type = "call"
    steps = 100
    american = False

    price = binomial_price(S, K, T, r, sigma, option_type, steps, american)
    assert price > 0
    # European Binomial should be close to Black-Scholes value
    assert abs(price - 10.45) < 0.5

def test_binomial_put_american():
    S = 100
    K = 100
    T = 1.0
    r = 0.05
    sigma = 0.2
    option_type = "put"
    steps = 100
    american = True

    price = binomial_price(S, K, T, r, sigma, option_type, steps, american)
    assert price > 0
    # American put usually priced slightly higher than European
    assert price >= 5.57

if __name__ == "__main__":
    pytest.main()
