# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 03:17:41 2023

@author: JosephRe
"""

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# FAANG stocks with gold for comparison
securities = ['META', 'AMZN', 'AAPL', 'NFLX', 'GOOG', 'GLD']

# Create and populate DataFrame with all closing prices for the securities since 2018-01-01
data = pd.DataFrame()
for security_name in securities:
    security = yf.Ticker(security_name)
    security = security.history(start='2018-01-01', end='2023-01-01')
    security = security['Close']
    data.insert(len(data.columns), security_name, security)
data = data.resample('BM').last()

# Create a monthly change in security price DataFrame
change = pd.DataFrame()
for month in data:
    if month not in change:
        change[month] = np.log(data[month]).diff()

# Print correlation matrix
corr = change.corr()
print(corr, end='\n\n')

# Print gold's correlations in sorted order
gold_corr = corr['GLD'].sort_values(ascending=False)
print(gold_corr)

# Create scattor plots for the correlation matrix
plot = pd.plotting.scatter_matrix(change, diagonal='kde', figsize=(12,12))
new_labels = [round(float(i.get_text()), 2) for i in plot[0,0].get_yticklabels()]
plot[0,0].set_yticklabels(new_labels)
plt.suptitle('FAANG + Gold Correlation Scatter Matrix', y=0.90)
plt.savefig(r'faang_correlation_scatter_matrix.png', bbox_inches='tight')