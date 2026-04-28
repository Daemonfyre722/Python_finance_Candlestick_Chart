# Python_finance
# Stock Candlestick Visualization

This project fetches historical stock data for Apple (AAPL) and visualizes it using a candlestick chart. The goal is to represent price movements in a format commonly used in trading and technical analysis.

## What this project does

The script retrieves daily stock data and transforms it into a candlestick chart showing Open, High, Low, and Close prices over time.

## Tools and libraries used

* Python
* yfinance – for fetching market data
* matplotlib – for plotting
* mplfinance – for candlestick visualization

## How it works

1. Define a time range for the data
2. Download AAPL stock data using Yahoo Finance
3. Extract and clean OHLC values
4. Convert date values into a format compatible with matplotlib
5. Plot the data as a candlestick chart
6. Apply styling for a dark-themed visualization

## Output

The final output is a candlestick chart where:

* Green candles indicate price increase (close > open)
* Red candles indicate price decrease (close < open)
* Wicks show the high and low range for each day

## Purpose

This project was built to practice working with financial time series data and to explore basic market visualization techniques in Python.
