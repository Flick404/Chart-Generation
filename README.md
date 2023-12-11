# Stock Analysis Tool

## Overview

This tool is designed to allow users to input a stock name or description, identify the corresponding ticker symbol, and visualize the stock's historical data through various technical indicators and Heikin-Ashi candlestick charts.

## Features

- **Ticker Recognition:** Processes user input to determine the appropriate stock ticker symbol.
- **Data Visualization:** Generates and displays Heikin-Ashi candlestick charts with additional technical indicators such as RSI and moving averages.
- **Historical Analysis:** Provides insights into stock performance over the past year.

## Installation

```bash
git clone [https://github.com/yourusername/stock-analysis-tool](https://github.com/Flick404/Chart-Generation)
cd stock-analysis-tool
pip install -r requirements.txt
```
## Usage
Run the program using the following command and follow the on-screen prompts:

```bash
python main.py
Environment Variables
Ensure that your .env file contains the following variable:
```

OPENAI_API_KEY: Your API key for OpenAI to use the GPT model.
## Code Documentation
### main.py
This script serves as the entry point for the application. It orchestrates the workflow of the tool.

```python
import chart
import ticker_recognition
```
The main function controls the application's flow, asking for user input and invoking other modules to process the input and plot data.

```python
def main():
    user_input = input("Please enter the name or description of a stock: ")
    ticker_symbol = ticker_recognition.get_ticker_symbol(user_input)
    chart.plot_stock_data(ticker_symbol)

if __name__ == "__main__":
    main()

```
### chart.py
This module includes functions for fetching stock data and plotting the chart.

Fetching historical data and preparing the Heikin-Ashi DataFrame:

```python
import yfinance as yf
import mplfinance as mpf
from datetime import datetime, timedelta
import pandas as pd

def plot_stock_data(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    # Fetch historical data for the last 1 year
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    data = stock.history(start=start_date.strftime("%Y-%m-%d"), end=end_date.strftime("%Y-%m-%d"))
    
    # ... additional processing ...
```
Calculating Heikin-Ashi candlesticks:

```python
def heikin_ashi(df):
    # ... code to calculate Heikin-Ashi candlesticks ...
```
Calculating RSI:

```python
def compute_rsi(data, window=14):
    # ... code to compute RSI ...
```
Final plotting with Moving Averages and RSI:
```python
    # ... continued from plot_stock_data
    ha_data = heikin_ashi(data)
    ha_data['MA50'] = ha_data['Close'].rolling(window=50).mean()
    ha_data['MA200'] = ha_data['Close'].rolling(window=200).mean()
    ha_data['RSI'] = compute_rsi(ha_data)
    
    # ... additional plotting setup ...
    mpf.plot(ha_data, type='candle', style='charles', addplot=apds, title=f'{ticker_symbol} Heikin-Ashi Chart', volume=False, figratio=(12,8), panel_ratios=(4,1))

```
### ticker_recognition.py

This module leverages the OpenAI API to recognize stock ticker symbols from descriptions.

Loading environment variables and initializing the OpenAI client:

```python
from openai import OpenAI
import os
from dotenv import load_dotenv

def get_ticker_symbol(user_input):
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    
    # Ensure API key is available
    if not api_key:
        raise ValueError("OpenAI API key not found in environment variables")
    
    client = OpenAI(api_key=api_key)
    # ... additional processing ...
```
Making the OpenAI API call to get the ticker symbol:

```python
    # ... continued from get_ticker_symbol
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Can you provide me with the Yahoo Finance ticker symbol for '{user_input}'? Please respond only with the ticker symbol."}
        ],
        # ... other parameters ...
    )
    
    ticker = response.choices[0].message.content.strip()
    return ticker
```


## Contributing
Contributions to the Goggins Telegram Bot are welcome. Please follow the standard fork-and-pull request workflow.
