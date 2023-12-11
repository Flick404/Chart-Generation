# Stock Analysis Tool

## Overview

This tool is designed to allow users to input a stock name or description, identify the corresponding ticker symbol, and visualize the stock's historical data through various technical indicators and Heikin-Ashi candlestick charts.

## Features

- **Ticker Recognition:** Processes user input to determine the appropriate stock ticker symbol.
- **Data Visualization:** Generates and displays Heikin-Ashi candlestick charts with additional technical indicators such as RSI and moving averages.
- **Historical Analysis:** Provides insights into stock performance over the past year.

## Installation

```ash
git clone https://github.com/yourusername/stock-analysis-tool
cd stock-analysis-tool
pip install -r requirements.txt
Usage
Run the program using the following command and follow the on-screen prompts:

bash
Copy code
python main.py
Environment Variables
Ensure that your .env file contains the following variable:

OPENAI_API_KEY: Your API key for OpenAI to use the GPT model.
Code Documentation
main.py
This script serves as the entry point for the application.

python
Copy code
import chart
import ticker_recognition

def main():
    user_input = input("Please enter the name or description of a stock: ")
    ticker_symbol = ticker_recognition.get_ticker_symbol(user_input)
    chart.plot_stock_data(ticker_symbol)

if __name__ == "__main__":
    main()
chart.py
This module handles data fetching and visualization.

python
Copy code
import yfinance as yf
import mplfinance as mpf
# ... other imports ...

def plot_stock_data(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    # Fetch and process data
    # ... code to fetch and process data ...
    mpf.plot(ha_data, type='candle', style='charles', addplot=apds, title=f'{ticker_symbol} Heikin-Ashi Chart', volume=False, figratio=(12,8), panel_ratios=(4,1))
ticker_recognition.py
This module uses the OpenAI API to recognize stock ticker symbols.

python
Copy code
from openai import OpenAI
# ... other imports ...

def get_ticker_symbol(user_input):
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    # Ensure API key is available
    # ... code to ensure API key ...
    response = client.chat.completions.create(
        model="gpt-4",
        # ... code to create chat completion ...
    )
    ticker = response.choices[0].message.content.strip()
    return ticker
Contributing
