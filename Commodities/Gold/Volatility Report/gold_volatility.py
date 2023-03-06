# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 21:20:50 2023

@author: JosephRe
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Imports gold ticker from yahoo finance and manipulates data to be usable
gold = yf.Ticker('GLD')
data = gold.history(start='2013-01-01', end='2023-01-01')
data = data.drop('Dividends', axis=1)
data = data.drop('Stock Splits', axis=1)
data = data.drop('Capital Gains', axis=1)
data = round(data, 2)
data = data.resample('BM').last()

# Creates a line-graph showing gold's price changes since 2013
with plt.style.context('ggplot'):
    plt.title('Price of Gold Since 2013')
    plt.ylabel('Close Price (USD)')
    plt.xlabel('Year')
    plt.plot(data.Close)
    plt.savefig('gold_price_since_2013.png', bbox_inches='tight')
    
# Logarithmic Transformation: Adds columns showing the natural log of percent change
data['Change'] = data['Close'] - data['Close'].shift()
data['LN_Change'] = np.log(data['Close'] / data['Close'].shift())

# Creates a histogram showing density of gold price changes by percentage
with plt.style.context('ggplot'):
    plt.figure(figsize=(10,8))
    plt.hist(data.LN_Change[:], bins=50, edgecolor='black', density=True)
    plt.title('Price Changes of Gold Since 2013')
    plt.ylabel('Number of Months')
    plt.xlabel('LN Delta (Based on Close Price)')
    plt.savefig('gold_volatility_report.png', bbox_inches='tight')