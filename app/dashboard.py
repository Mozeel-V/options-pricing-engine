# app/dashboard.py

import streamlit as st
import matplotlib.pyplot as plt
from data_fetcher import get_spot_price_and_volatility
from utils import time_to_expiry
from pricing import black_scholes_price, binomial_price, monte_carlo_barrier_option, monte_carlo_asian_option
from plot_helpers import plot_price_vs_strike, plot_price_vs_volatility

def main():
    st.set_page_config(page_title="Options Pricing Engine", layout="centered")
    st.title("📈 Options Pricing Engine")
    st.markdown("Supports **Call** and **Put** options. European by Black-Scholes-Merton model, American by Binomial Tree, Exotic options by Monte Carlo Simulation.")

    st.sidebar.header("Input Parameters")

    # User Inputs
    ticker = st.sidebar.text_input("Stock Ticker (e.g., AAPL, INFY.NS)", value="AAPL")
    strike = st.sidebar.number_input("Strike Price", min_value=0.0, value=150.0, step=1.0)
    expiry = st.sidebar.text_input("Expiry Date (YYYY-MM-DD)", value="2025-06-20")
    risk_free_rate = st.sidebar.number_input("Risk-Free Rate (e.g. 0.06 = 6%)", min_value=0.0, value=0.06, step=0.01)
    option_style = st.sidebar.selectbox("Option Style", ["European", "American", "Barrier", "Asian"])
    option_type = st.sidebar.selectbox("Option Type", ["call", "put"])

    # Conditional Inputs

    if option_style == "Barrier":
        direction = st.sidebar.selectbox("Barrier Direction", ["up", "down"])
        knock = st.sidebar.selectbox("Knock Type", ["in", "out"])
        barrier_level = st.sidebar.number_input("Barrier Level", min_value=0.0, value=170.0, step=1.0)

    elif option_style == "Asian":
        asian_type = st.sidebar.selectbox("Asian Type", ["arithmetic", "geometric"])

    viz_type = st.sidebar.selectbox("Select visualization", ["None", "Price vs Strike", "Price vs Volatility"])
    calculate = st.sidebar.button("Calculate Option Price")

    if calculate:
        try:
            # st.info("Fetching data and computing price...")

            S, sigma = get_spot_price_and_volatility(ticker)
            S = float(S)
            sigma = float(sigma)
            T = time_to_expiry(expiry)

            if option_style == "European":
                price = black_scholes_price(S, strike, T, risk_free_rate, sigma, option_type)
            elif option_style == "American":
                price = binomial_price(S, strike, T, risk_free_rate, sigma, option_type, steps=100, american=True)
            elif option_style == "Barrier":
                price = monte_carlo_barrier_option(
                    S0=S,
                    K=strike,
                    r=risk_free_rate,
                    sigma=sigma,
                    T=T,
                    barrier=barrier_level,
                    option_type=option_type,
                    knock=knock,
                    direction=direction
                )
            elif option_style == "Asian":
                price = monte_carlo_asian_option(
                    S0=S,
                    K=strike,
                    r=risk_free_rate,
                    sigma=sigma,
                    T=T,
                    option_type=option_type
                )

            st.success(f"**{option_type.capitalize()} {option_style} Option Price:** ${price:.2f}")
            st.write(f"**Spot Price:** ${S:.2f}")
            st.write(f"**Volatility (1Y):** {sigma*100:.2f}%")
            st.write(f"**Time to Expiry:** {T*365:.0f} days")

            if viz_type == "Price vs Strike":
                fig = plot_price_vs_strike(S, T, risk_free_rate, sigma, option_type)
                st.pyplot(fig)
            elif viz_type == "Price vs Volatility":
                fig = plot_price_vs_volatility(S, strike, T, risk_free_rate, option_type)
                st.pyplot(fig)

        except Exception as e:
            st.error(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
