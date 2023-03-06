# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 22:28:34 2023

@author: JosephRe
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Imports gold ticker from yahoo finance, cleans up data, and adds 5-day moving average
gold = yf.Ticker('GLD')
data = gold.history(start='2022-01-01', end='2022-12-31')
data = data.drop('Dividends', axis=1)
data = data.drop('Stock Splits', axis=1)
data = data.drop('Capital Gains', axis=1)
data = round(data, 2)
data['5-day'] = data['Close'].rolling(5).mean().shift()

# Creates a line-graph showing 5-day moving average for all of 2022
with plt.style.context('ggplot'):
    plt.title('Gold Moving Average Forecast (2022)')
    plt.ylabel('Close Price (USD)')
    plt.xlabel('Time')
    plt.plot(data.Close, label='Actual Close')
    plt.plot(data['5-day'], label='5-Day Moving Avg.')
    plt.legend(loc=1)
    plt.savefig('gold_moving_average_forecast.png', bbox_inches='tight')

# Error Measure Calculations Below
# Mean Absolute Deviation
data['MAD'] = np.abs(data['Close']-data['5-day'])

# Mean Absolute Percent Error
data['MAPE'] = data['MAD'] / data['Close']

# Mean Squared Error
data['MSE'] = data['MAD'] ** 2
MSE = data['MSE'].mean()
RMSE = np.sqrt(MSE)

# Print Error Summary
print(f"Mean Absolute Deviation = {data['MAD'].mean()}")
print(f"Mean Absolute Percent Error = {data['MAPE'].mean()}")
print(f"Mean Squared Error = {MSE}")
print(f"Root Mean Squared Error = {RMSE}")
