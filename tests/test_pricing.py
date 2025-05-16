# tests/test_pricing.py

import pytest
from app.pricing import (
    black_scholes_price,
    binomial_price,
    monte_carlo_asian_option,
    monte_carlo_barrier_option
)

def test_black_scholes_call():
    S, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.2
    price = black_scholes_price(S, K, T, r, sigma, "call")
    assert price > 0
    assert round(price, 2) == 10.45

def test_black_scholes_put():
    S, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.2
    price = black_scholes_price(S, K, T, r, sigma, "put")
    assert price > 0
    assert round(price, 2) == 5.57

def test_binomial_call_european():
    S, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.2
    price = binomial_price(S, K, T, r, sigma, "call", steps=100, american=False)
    assert price > 0
    assert abs(price - 10.45) < 0.5

def test_binomial_put_american():
    S, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.2
    price = binomial_price(S, K, T, r, sigma, "put", steps=100, american=True)
    assert price > 0
    assert price >= 5.57  # American puts are worth at least as much as European

def test_monte_carlo_asian_call():
    S, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.2
    price = monte_carlo_asian_option(S, K, r, sigma, T, steps=100, paths=5000, option_type="call")
    assert price > 0
    assert price < black_scholes_price(S, K, T, r, sigma, "call")  # Asian <= European

def test_monte_carlo_barrier_up_out_call():
    S, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.2
    barrier = 110
    knock, direction = "out", "up"
    price = monte_carlo_barrier_option(S, K, r, sigma, T, barrier, steps=100, paths=5000, option_type="call", knock=knock, direction=direction)
    assert price >= 0
    assert price < black_scholes_price(S, K, T, r, sigma, "call")  # Knock-out less value


if __name__ == "__main__":
    pytest.main()
