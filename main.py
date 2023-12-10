import chart
import ticker_recognition

def main():
    # Ask user for the stock name or description
    user_input = input("Please enter the name or description of a stock: ")

    # Get the ticker symbol using ticker_recognition
    ticker_symbol = ticker_recognition.get_ticker_symbol(user_input)

    # Fetch and plot data for the obtained ticker symbol
    chart.plot_stock_data(ticker_symbol)

if __name__ == "__main__":
    main()
