# Options Pricing Engine

A simple and interactive European Options Pricing Engine built with Python.  
Supports **Call** and **Put** options priced using the **Black-Scholes model**.

---

## 🚀 Features

- Fetches **spot price** and **1-year historical volatility** automatically from Yahoo Finance using the stock ticker.
- Takes **strike price**, **expiry date**, and **risk-free rate** as user inputs.
- Calculates **time to expiry** in years.
- Supports both **European call** and **put** options.
- Provides a clean **Streamlit dashboard** for interactive pricing.
- CLI fallback available for quick testing.

---

## 🛠️ Project Structure

```bash
options-pricing-engine/
├── app/
│   ├── __init__.py
│   ├── pricing.py           # Black-Scholes formulas
│   ├── data_fetcher.py      # Spot price, volatility from yfinance
│   ├── dashboard.py         # Streamlit UI
│   └── utils.py             # Helpers (e.g. days to expiry)
├── notebooks/
│   └── analysis.ipynb       # EDA + plots
├── tests/
│   └── test_pricing.py      # Unit tests for formulas
├── main.py                  # Entry point for running CLI version
├── requirements.txt         # All required packages
├── directory_structure.txt  # This file
├── .gitignore
└── README.md
```

---

## ⚙️ How to Run

### 1. Clone the repository on your local machine
```bash
git clone https://github.com/Mozeel-V/options-pricing-engine.git
```

### 2. Install dependencies in your python environment
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit dashboard (recommended)
```bash
streamlit run app/dashboard.py
```
This will open a web UI where you can input parameters and get option prices interactively.

### 4. Alternatively, you can run the CLI (Command-Line Interface) tool (basic)
```bash
python main.py
```
Follow the prompts to input ticker, strike, expiry, risk-free rate, and option type.

---

## 🧮 Black-Scholes Model

The engine uses the Black-Scholes formula to price European options:
- Inputs: Spot price (S), Strike price (K), Time to expiry (T), Risk-free rate (r), Volatility (σ), Option type (call/put).
- Outputs: Option price.
Volatility is calculated as the annualized standard deviation of daily log returns over the past 1 year.

---

## ✅ How to run the tests

Install pytest if not already:
```bash
pip install pytest
```
Run from the root directory:
```bash
pytest tests/
```
It’ll run both tests and show PASSED if your pricing logic is correct

---

## 🔗 Notes

- Risk-free rate input is manual because real-time fetching requires paid APIs.

- Expiry date format must be YYYY-MM-DD.

- Supports only European options currently.

- The project can be extended with Greeks calculation, American options, and more.

---

## 🤝 Contributions

Feel free to fork, raise issues, or submit PRs to improve this project!

---

## 📝 Author
Mozeel Vanwani | IIT Kharagpur CSE
Email: [vanwani.mozeel@gmail.com]