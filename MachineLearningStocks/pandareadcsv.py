import os
from pandas_datareader import data as pdr
import pandas as pd
import fix_yahoo_finance as yf
START_DATE = "2001-01-01"
END_DATE = "2019-28-07"
def build_stock_dataset(start=START_DATE, end=END_DATE):
    """
    Creates the dataset containing all stock prices
    :returns: stock_prices.csv
    """

    statspath = "intraQuarter/_KeyStats/"
    ticker_list = os.listdir(statspath)

    # Required on macOS
    if ".DS_Store" in ticker_list:
        os.remove(f"{statspath}/.DS_Store")
        ticker_list.remove(".DS_Store")

    # Get all Adjusted Close prices for all the tickers in our list,
    # between START_DATE and END_DATE
    all_data = pdr.get_data_yahoo(ticker_list, start, end)
    stock_data = all_data["Adj Close"]

    # Remove any columns that hold no data, and print their tickers.
    stock_data.dropna(how="all", axis=1, inplace=True)
    missing_tickers = [
        ticker for ticker in ticker_list if ticker.upper() not in stock_data.columns
    ]
    print(f"{len(missing_tickers)} tickers are missing: \n {missing_tickers} ")
    # If there are only some missing datapoints, forward fill.
    stock_data.ffill(inplace=True)
    stock_data.to_csv("stock_prices.csv")
	
if __name__ == "__main__":
    build_stock_dataset()

