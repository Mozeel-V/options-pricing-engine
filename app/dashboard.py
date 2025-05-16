# app/dashboard.py

import streamlit as st
from app.data_fetcher import get_spot_price_and_volatility
from app.utils import time_to_expiry
from app.pricing import black_scholes_price

def main():
    st.set_page_config(page_title="Options Pricing Engine", layout="centered")
    st.title("📈 European Options Pricing Engine")
    st.markdown("Supports **Call** and **Put** options using the Black-Scholes model.")

    st.sidebar.header("Input Parameters")

    # User Inputs
    ticker = st.sidebar.text_input("Stock Ticker (e.g., AAPL, INFY.NS)", value="AAPL")
    strike = st.sidebar.number_input("Strike Price", min_value=0.0, value=150.0, step=1.0)
    expiry = st.sidebar.text_input("Expiry Date (YYYY-MM-DD)", value="2025-06-20")
    risk_free_rate = st.sidebar.number_input("Risk-Free Rate (e.g. 0.06 = 6%)", min_value=0.0, value=0.06, step=0.01)
    option_type = st.sidebar.selectbox("Option Type", ["call", "put"])

    if st.sidebar.button("Calculate Option Price"):
        try:
            st.info("Fetching data and computing price...")

            S, sigma = get_spot_price_and_volatility(ticker)
            T = time_to_expiry(expiry)
            price = black_scholes_price(S, strike, T, risk_free_rate, sigma, option_type)

            st.success(f"**{option_type.capitalize()} Option Price:** ${price:.2f}")
            st.write(f"**Spot Price:** ${S:.2f}")
            st.write(f"**Volatility (1Y):** {sigma*100:.2f}%")
            st.write(f"**Time to Expiry:** {T*365:.0f} days")
        except Exception as e:
            st.error(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
