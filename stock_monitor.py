import pandas as pd
import matplotlib.pyplot as pltnction to get and display stock information ---
def get_stock_data(ticker_symbol):
    """
    Fetches and displays key stock information and plots historical data.

    Args:
        ticker_symbol (str): The ticker symbol of the stock (e.g., 'AAPL' for Apple).
    """
    try:
        # Create a Ticker object for the stock
        stock = yf.Ticker(ticker_symbol)

        # Get key information about the stock
        info = stock.info
        
        # Check if the info dictionary is populated
        if not info or 'regularMarketPrice' not in info:
            print(f"Error: Could not retrieve data for the ticker symbol '{ticker_symbol}'.")
            return

        # Print the current stock information
        print(f"\n--- Stock Price Information for {info.get('longName', 'N/A')} ({ticker_symbol}) ---")
        print(f"Current Price: ${info.get('regularMarketPrice', 'N/A'):.2f}")
        print(f"Previous Close: ${info.get('previousClose', 'N/A'):.2f}")
        print(f"Open: ${info.get('regularMarketOpen', 'N/A'):.2f}")
        print(f"Day's High: ${info.get('dayHigh', 'N/A'):.2f}")
        print(f"Day's Low: ${info.get('dayLow', 'N/A'):.2f}")
        print(f"Market Cap: {info.get('marketCap', 'N/A'):,}")
        print("-" * 50)

        # Fetch historical data for the last 1 year
        historical_data = stock.history(period="1y")

        # Check if historical data is available
        if historical_data.empty:
            print("No historical data available for this ticker.")
            return

        # Plot the historical closing prices
        plt.figure(figsize=(10, 6))
        plt.plot(historical_data['Close'], label='Closing Price', color='dodgerblue')
        plt.title(f"Historical Stock Price for {info.get('longName', ticker_symbol)} (Last 1 Year)")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.grid(True)
        plt.legend()
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check the ticker symbol and your internet connection.")

# --- Main part of the script ---
if __name__ == "__main__":
    # Prompt the user for a stock ticker symbol
    ticker_input = input("Enter a stock ticker symbol (e.g., AAPL, GOOG, TSLA): ").upper()
    
    # Call the function to get and display the data
    get_stock_data(ticker_input)
