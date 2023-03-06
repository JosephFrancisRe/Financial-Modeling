# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 00:20:08 2023

@author: JosephRe
"""

import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download('NVDA', start='2019-01-01', end='2023-01-01')
data.drop('Adj Close', axis=1, inplace=True)

data['9-day'] = data['Close'].rolling(9).mean()
data['21-day'] = data['Close'].rolling(21).mean() 
data['Change'] = np.log(data.Close / data.Close.shift())

with plt.style.context('ggplot'):
    plt.figure(0, figsize=(8,6))
    plt.plot(data.Close[:])
    plt.plot(data['9-day'][:], label='9-day moving average')
    plt.plot(data['21-day'][:], label='21-day moving average')
    plt.legend(loc=2)
    plt.title('NVIDIA Stock Price Moving Averages')
    plt.ylabel('Close Price (USD)')
    plt.xlabel('Time')
    plt.savefig('moving_averages_nvidia.png', bbox_inches='tight')

# Add position to the dataframe (1 = long, -1 = short, 0 = no position)
data['position'] = np.where(data['9-day'] > data['21-day'], 1, 0)
data['position'] = np.where(data['9-day'] < data['21-day'], -1, data['position'])

# Calculate and plot change
data['Trading System'] = data['position'] * data['Change']
plt.figure(1)
plt.plot(data['Change'].cumsum(), label='Actual')
plt.plot(data['Trading System'].cumsum(), label='Trading System')
plt.legend(loc=2)
plt.title('NVIDIA Actual Change vs. Moving Average Trading System')
plt.ylabel('Close Price (USD)')
plt.xlabel('Percentage Change')
plt.savefig('percent_change_actual_vs_trading_system.png', bbox_inches='tight')