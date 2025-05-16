# app/utils.py

from datetime import datetime

def time_to_expiry(expiry_date_str):
    """
    Calculates time to expiry in years.

    Parameters:
    expiry_date_str : str in format 'YYYY-MM-DD'

    Returns:
    T : float (years)
    """
    try:
        expiry = datetime.strptime(expiry_date_str, "%Y-%m-%d")
        today = datetime.today()
        delta_days = (expiry - today).days
        return max(delta_days / 365.0, 0.0)
    except Exception as e:
        raise ValueError("Invalid expiry date format. Use YYYY-MM-DD.") from e
