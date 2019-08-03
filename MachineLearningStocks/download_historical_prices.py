import os
from pandas_datareader import data as pdr
import pandas as pd
import yfinance as yf
import csv

# yf.pdr_override()

START_DATE = "2001-01-01"
END_DATE = "2019-07-28"


def build_stock_dataset(start=START_DATE, end=END_DATE):
    # csv file name
    # reading csv file
    with open("snp10.csv", 'r') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=",")
        csvreader = csv.reader(csvfile)
        ticker_list = list()
        for row in csvReader:
            ticker_list.append((row[2]))
    all_data = yf.download(ticker_list, period='max', treads=True)
    stock_data = all_data["Adj Close"]
    # Remove any columns that hold no data, and print their tickers.
    stock_data.dropna(how="all", axis=1, inplace=True)
    missing_tickers = [
        ticker for ticker in ticker_list if ticker not in stock_data.columns
    ]
    print(f"{len(missing_tickers)} tickers are missing: \n {missing_tickers} ")
    If there are only some missing datapoints, forward fill.
    stock_data.ffill(inplace=True)
    stock_data.to_csv("stock_prices.csv")


def build_sp500_dataset(start=START_DATE, end=END_DATE):
    """
    Creates the dataset containing S&P500 prices
    :returns: sp500_index.csv
    """
    # index_data = pdr.get_data_yahoo("SPY", start, end)
    index_data = yf.download("SPY", period='max', treads=True)
    index_data.to_csv("sp500_index.csv")


def build_dataset_iteratively(idx_start, idx_end, date_start=START_DATE, date_end=END_DATE):
    with open("SNP500.csv", 'r') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=",")
        csvreader = csv.reader(csvfile)
        ticker_list = list()
        for row in csvReader:
            ticker_list.append(row[2])
        all_data = yf.download(ticker_list, period='max', treads=True)
        stock_data = all_data["Adj Close"]

    # Remove any columns that hold no data, and print their tickers.
    stock_data.dropna(how="all", axis=1, inplace=True)
    missing_tickers = [
        ticker for ticker in ticker_list if ticker not in stock_data.columns
    ]
    print(f"{len(missing_tickers)} tickers are missing: \n {missing_tickers} ")
    # If there are only some missing datapoints, forward fill.
    stock_data.ffill(inplace=True)
    stock_data.to_csv("stock_prices.csv")

    df = pd.DataFrame()

    for ticker in ticker_list:

        stock_ohlc = pdr.get_data_yahoo(ticker, start=date_start, end=date_end)
        if stock_ohlc.empty:
            print(f"No data for {ticker}")
            continue
        adj_close = stock_ohlc["Adj Close"].rename(ticker)
        df = pd.concat([df, adj_close], axis=1)
    df.to_csv("stock_prices.csv")


if __name__ == "__main__":
    build_stock_dataset()
    build_sp500_dataset()
