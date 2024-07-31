import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def calculate_moving_averages(stock_data, short_window=40, long_window=100):
    stock_data['Short_Moving_Avg'] = stock_data['Close'].rolling(window=short_window, min_periods=1).mean()
    stock_data['Long_Moving_Avg'] = stock_data['Close'].rolling(window=long_window, min_periods=1).mean()
    return stock_data

def plot_stock_data(stock_data, ticker):
    plt.figure(figsize=(12, 8))
    plt.plot(stock_data['Close'], label='Close Price')
    plt.plot(stock_data['Short_Moving_Avg'], label=f'{short_window}-Day Moving Average')
    plt.plot(stock_data['Long_Moving_Avg'], label=f'{long_window}-Day Moving Average')
    plt.title(f'Stock Price and Moving Averages for {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Define stock ticker, start date, and end date
    ticker = str(input("Enter the ticker name : ")   #'AAPL'
    start_date = input("Start Date : yyyy-mm-dd")  # '2022-01-01'
    end_date = input("End Date : yyyy-mm-dd")  #'2023-01-01'

    # Fetch stock data
    stock_data = fetch_stock_data(ticker, start_date, end_date)

    # Calculate moving averages
    short_window = 40
    long_window = 100
    stock_data = calculate_moving_averages(stock_data, short_window, long_window)

    # Plot the data
    plot_stock_data(stock_data, ticker)
