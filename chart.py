import yfinance as yf
import mplfinance as mpf
from datetime import datetime, timedelta
import pandas as pd

# Function to calculate Heikin-Ashi candlesticks
def heikin_ashi(df):
    df_ha = df.copy()
    df_ha['Close'] = (df['Open'] + df['High'] + df['Low'] + df['Close']) / 4

    ha_open = [(df['Open'].iloc[0] + df['Close'].iloc[0]) / 2]
    for i in range(1, len(df)):
        new_open = (ha_open[i-1] + df_ha['Close'].iloc[i-1]) / 2
        ha_open.append(new_open)

    df_ha['Open'] = ha_open
    df_ha['High'] = df[['Open', 'Close', 'High']].max(axis=1)
    df_ha['Low'] = df[['Open', 'Close', 'Low']].min(axis=1)

    return df_ha

# Function to calculate RSI
def compute_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Function to plot stock data
def plot_stock_data(ticker_symbol):
    # Fetch historical data for the last 1 year
    stock = yf.Ticker(ticker_symbol)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    data = stock.history(start=start_date.strftime("%Y-%m-%d"), end=end_date.strftime("%Y-%m-%d"))

    # Calculate Heikin-Ashi DataFrame
    ha_data = heikin_ashi(data)

    # Calculate Moving Averages
    ha_data['MA50'] = ha_data['Close'].rolling(window=50).mean()
    ha_data['MA200'] = ha_data['Close'].rolling(window=200).mean()

    # Calculate RSI
    ha_data['RSI'] = compute_rsi(ha_data)

    # Drop rows where RSI or MAs are NaN (typically the first 200 rows)
    ha_data = ha_data.iloc[200:]

    # Create an `mpf.make_addplot()` list for MAs and RSI
    apds = [mpf.make_addplot(ha_data['MA50'], color='blue'),
            mpf.make_addplot(ha_data['MA200'], color='purple'),  # MA200 line color changed to purple
            mpf.make_addplot(ha_data['RSI'], panel=1, color='orange', ylabel='RSI', ylim=(0, 100))]  # Set RSI y-axis limits

    # Adjust panel_ratios to make the RSI panel smaller
    mpf.plot(ha_data, type='candle', style='charles', addplot=apds, title=f'{ticker_symbol} Heikin-Ashi Chart', volume=False, figratio=(12,8), panel_ratios=(4,1))