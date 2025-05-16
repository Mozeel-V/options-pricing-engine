# Options Pricing Engine

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3670A0?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit App](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/Tested%20with-Pytest-6DB33F?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Status](https://img.shields.io/badge/Build-Active-blue)]()

A simple and interactive European Options Pricing Engine built with Python. 
Supports **European, American, Asian, and Barrier** options using mathematical models like **Black-Scholes**, **Binomial Tree**, and **Monte Carlo simulation**.

---

## 🚀 Features

- Fetches **spot price** and **1-year historical volatility** automatically from Yahoo Finance using the stock ticker.
- Supports:
  - **European** (Call/Put) via Black-Scholes
  - **American** (Call/Put) via Binomial Tree
  - **Asian options** (Call/Put) via Monte Carlo simulation
  - **Barrier options** (Call/Put – up-out/down-out) via Monte Carlo
- Takes **strike price**, **expiry date**, and **risk-free rate** as user inputs.
- Auto-calculates **time to expiry** in years.
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
│   ├── pricing.py           # Black-Scholes, Binomial Tree, and Monte Carlo Simulation logic
│   ├── plot_helpers.py      # For visualization using matplotlib
│   ├── data_fetcher.py      # Spot price and volatility from yfinance
│   ├── dashboard.py         # Streamlit UI
│   └── utils.py             # Helpers (e.g. days to expiry)
├── notebooks/
│   └── analysis.ipynb       # Exploratory testing + plots
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

## 🧮 Pricing Models Used

- **Black-Scholes Model** (for European Options)  
  Calculates theoretical prices for **European call and put options** using a closed-form formula.  
  **Inputs:** Spot Price (S), Strike Price (K), Time to Expiry (T), Risk-Free Rate (r), Volatility (σ), Option Type (call/put)  
  **Volatility** is computed from 1-year historical data as the annualized standard deviation of daily log returns.

- **Binomial Tree Model** (for American & European Options)  
  Uses a discrete-time lattice to model option price evolution, suitable for options with early exercise features like **American options**.  
  **Customizable steps** allow precision tuning.

- **Monte Carlo Simulation** (for Exotic Options)  
  Supports pricing of **Asian options** (average price) and **Barrier options** (knock-in, knock-out) by simulating many possible stock price paths and averaging discounted payoffs.  
  Flexible and powerful for options without closed-form solutions.


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
It’ll run all tests and show PASSED if our pricing logic is correct

---

## 🔗 Notes

- Risk-free rate input is manual because real-time fetching requires paid APIs.

- Expiry date format must be YYYY-MM-DD.

- Monte Carlo options require longer run-time (use ~5000+ simulations).

- The project can be extended with Greeks calculation and visualizations, implied volatility, stochastic volatility modelling and more.

---

## 🤝 Contributions

Feel free to fork, raise issues, or submit PRs to improve this project!

---

## 📝 Author
Mozeel Vanwani | IIT Kharagpur CSE

Email: [vanwani.mozeel@gmail.com]