# AI Stock Market Analysis

## Overview

AI Stock Market Analysis is a Python-based project that collects stock market data, calculates technical indicators, stores historical data in MySQL, and generates AI-assisted stock analysis reports. It also includes interactive visualizations and a Power BI dashboard.

## Features

- Fetch historical stock market data using Yahoo Finance (`yfinance`).
- Search for stocks by company name.
- Store stock data in a MySQL database.
- Calculate technical indicators:
  - Simple Moving Average (SMA)
  - Exponential Moving Average (EMA)
  - Relative Strength Index (RSI)
  - Moving Average Convergence Divergence (MACD)
  - Bollinger Bands
- Retrieve financial news using the Marketaux API.
- Generate AI-assisted analysis reports using Google Gemini.
- Visualize stock prices and technical indicators with Plotly.
- Analyze stock performance using a Power BI dashboard.

## Technologies Used

- **Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Stock Data:** yfinance
- **Database:** MySQL
- **AI:** Google Gemini API
- **Financial News:** Marketaux API
- **Visualization:** Plotly, Microsoft Power BI

## Project Structure

```text
AI Stock Analysis/
├── app/
│   ├── ai.py
│   ├── analysis.py
│   ├── automation.py
│   ├── dashboard.py
│   ├── data.py
│   ├── database.py
│   ├── main.py
│   ├── news.py
│   ├── search.py
│   └── utils.py
├── .env                 # Local secrets; do not upload
├── .gitignore
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.12 or a compatible Python version
- MySQL Server
- Google Gemini API key
- Marketaux API key

## Setup

1. Clone or download this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and configure your API keys and database credentials.

   Example:

   ```env
   GEMINI_API_KEY=your_gemini_api_key
   MARKETAUX_API_KEY=your_marketaux_api_key
   DB_HOST=localhost
   DB_USER=your_mysql_username
   DB_PASSWORD=your_mysql_password
   DB_NAME=stock_market_ai
   ```

5. Create the `stock_market_ai` database and the required `stock_prices` table in MySQL, using the schema expected by `database.py`.

6. Run the application using the entry point configured in your project. If `main.py` is inside `app`, run it from the project root using the appropriate module command for your package structure.

## Usage

Enter a company name when prompted. The application fetches stock data, calculates technical indicators, updates the MySQL database, retrieves financial news, and generates an AI-assisted report. The dashboard displays stock price movements and technical indicators.

## Security

- Never commit `.env` or API keys to GitHub.
- Keep database credentials private.
- Use `.gitignore` to exclude secrets and the virtual environment.

## Disclaimer

This project is for educational and analytical purposes only. Its technical indicators and AI-generated reports are not guaranteed to predict future market performance and should not be treated as financial advice.
