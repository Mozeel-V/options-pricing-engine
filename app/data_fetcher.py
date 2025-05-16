# app/data_fetcher.py

import yfinance as yf
import numpy as np

def get_spot_price_and_volatility(ticker):
    """
    Fetches spot price and 1-year historical volatility for a given stock ticker.

    Parameters:
    ticker : str (e.g., 'AAPL', 'INFY.NS')

    Returns:
    spot_price : float
    volatility : float (annualized)
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period="1y")

    if data.empty or len(data['Close']) < 2:
        raise ValueError("Insufficient data to compute volatility.")

    spot_price = data['Close'].iloc[-1]

    # Daily log returns
    returns = np.log(data['Close'] / data['Close'].shift(1)).dropna()
    volatility = returns.std() * np.sqrt(252)  # Annualize

    return spot_price, volatility
