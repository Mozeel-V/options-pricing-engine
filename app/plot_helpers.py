# app/plot_helpers.py

import numpy as np
import matplotlib.pyplot as plt
from pricing import black_scholes_price

def plot_price_vs_strike(S, T, r, sigma, option_type):
    strikes = np.linspace(0.5 * S, 1.5 * S, 100)
    prices = [black_scholes_price(S, K, T, r, sigma, option_type) for K in strikes]

    fig, ax = plt.subplots()
    ax.plot(strikes, prices)
    ax.set_title("Option Price vs Strike Price")
    ax.set_xlabel("Strike Price")
    ax.set_ylabel("Option Price")
    ax.grid(True)
    return fig

def plot_price_vs_volatility(S, K, T, r, option_type):
    volatilities = np.linspace(0.05, 1.0, 100)
    prices = [black_scholes_price(S, K, T, r, sigma, option_type) for sigma in volatilities]

    fig, ax = plt.subplots()
    ax.plot(volatilities, prices)
    ax.set_title("Option Price vs Volatility")
    ax.set_xlabel("Volatility")
    ax.set_ylabel("Option Price")
    ax.grid(True)
    return fig
