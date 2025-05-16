# Options Pricing Engine

A simple and interactive European Options Pricing Engine built with Python.  
Supports **Call** and **Put** options priced using the **Black-Scholes model** for European options and the **Binomial Tree model** for American options.

---

## 🚀 Features

- Fetches **spot price** and **1-year historical volatility** automatically from Yahoo Finance using the stock ticker.
- Takes **strike price**, **expiry date**, and **risk-free rate** as user inputs.
- Calculates **time to expiry** in years.
- Supports both **European and American** option styles for **call** and **put** options.
- Interactive and clean **Streamlit dashboard** with input sidebar and visualization section.
- Visualizes option price sensitivity:
    - **Price vs Strike Price**
    - **Price vs Volatility**
- CLI fallback available for quick testing.

---

## 🛠️ Project Structure

```bash
options-pricing-engine/
├── app/
│   ├── __init__.py
│   ├── pricing.py           # Black-Scholes and Binomial Tree formulae
│   ├── plot_helpers.py      # For visualization using matplotlib
│   ├── data_fetcher.py      # Spot price, volatility from yfinance
│   ├── dashboard.py         # Streamlit UI
│   └── utils.py             # Helpers (e.g. days to expiry)
├── notebooks/
│   └── analysis.ipynb       # EDA + plots
├── tests/
│   └── test_pricing.py      # Unit tests for formulae
├── main.py                  # Entry point for running CLI version
├── requirements.txt         # All required packages
├── directory_structure.txt  # Maintains directory structure in an organized way
├── .gitignore               # Standard .gitignore for python projects
└── README.md                # This file
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
This opens a web UI for interactive option pricing and visualization.

### 4. Alternatively, you can run the CLI (Command-Line Interface) tool (basic)
```bash
python main.py
```
Follow the prompts to input ticker, strike, expiry, risk-free rate, and option type and get option prices.

---

## 🧮 Pricing Models used

- Black-Scholes Model for European options
Inputs: Spot price (S), Strike price (K), Time to expiry (T), Risk-free rate (r), Volatility (σ), Option type (call/put)
Output: Option price
Volatility is computed as annualized std deviation of daily log returns over 1 year.

- Binomial Tree Model for American options
Calculates price using a discrete-time lattice, accounting for early exercise feature unique to American options.

---

## 📊 Visualization

Price vs Strike Price: Shows how option price changes when varying strike price, holding other parameters fixed.

Price vs Volatility: Shows sensitivity of option price to changes in volatility, keeping other inputs constant.

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

- Supports both European and American options.

- The project can be extended with Greeks calculation and visualizations, and more.

---

## 🤝 Contributions

Feel free to fork, raise issues, or submit PRs to improve this project!

---

## 📝 Author
Mozeel Vanwani | IIT Kharagpur CSE

Email: [vanwani.mozeel@gmail.com]