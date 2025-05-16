# app/dashboard.py

import streamlit as st
import matplotlib.pyplot as plt
from data_fetcher import get_spot_price_and_volatility
from utils import time_to_expiry
from pricing import black_scholes_price, binomial_price
from plot_helpers import plot_price_vs_strike, plot_price_vs_volatility

def main():
    st.set_page_config(page_title="Options Pricing Engine", layout="centered")
    st.title("📈 Options Pricing Engine")
    st.markdown("Supports **Call** and **Put** options. European by Black-Scholes, American by Binomial Tree.")

    st.sidebar.header("Input Parameters")

    # User Inputs
    ticker = st.sidebar.text_input("Stock Ticker (e.g., AAPL, INFY.NS)", value="AAPL")
    strike = st.sidebar.number_input("Strike Price", min_value=0.0, value=150.0, step=1.0)
    expiry = st.sidebar.text_input("Expiry Date (YYYY-MM-DD)", value="2025-06-20")
    risk_free_rate = st.sidebar.number_input("Risk-Free Rate (e.g. 0.06 = 6%)", min_value=0.0, value=0.06, step=0.01)
    option_style = st.sidebar.selectbox("Option Style", ["European", "American"])
    option_type = st.sidebar.selectbox("Option Type", ["call", "put"])
    viz_type = st.sidebar.selectbox("Select visualization", ["None", "Price vs Strike", "Price vs Volatility"])

    calculate = st.sidebar.button("Calculate Option Price")

    if calculate:
        try:
            st.info("Fetching data and computing price...")

            S, sigma = get_spot_price_and_volatility(ticker)
            T = time_to_expiry(expiry)
            if option_style == "European":
                price = black_scholes_price(S, strike, T, risk_free_rate, sigma, option_type)
            else:
                price = binomial_price(S, strike, T, risk_free_rate, sigma, option_type, steps=100, american=True)

            st.success(f"**{option_type.capitalize()} Option Price:** ${price:.2f}") # premium paid to buy this contract
            st.write(f"**Spot Price:** ${S:.2f}")
            st.write(f"**Volatility (1Y):** {sigma*100:.2f}%")
            st.write(f"**Time to Expiry:** {T*365:.0f} days")
            # Visualization
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
