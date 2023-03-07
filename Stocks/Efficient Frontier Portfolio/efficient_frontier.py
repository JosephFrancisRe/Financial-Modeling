# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 02:38:43 2023

@author: JosephRe
"""

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define index and stocks to be put into a regression
stocks = ['AAPL', 'GLD']

# Create a dataframe and populate it with close values.
data = pd.DataFrame()
count = 0
for stock in stocks:
    value = yf.download(stock, start='2022-03-01', end='2023-03-02')['Close']
    data.insert(count, column=stock, value=value)
    count += 1
    
print(data.info())

# Create dataframe with the natural log change
change = pd.DataFrame()
for column in data:
    if column not in change:
        change[column] = np.log(data[column]).diff()
change = change.dropna()

print(change)

# Annualized variance
var_aapl = change['AAPL'].var() * 252
var_gld = change['GLD'].var() * 252

print(f"Apple variance: {var_aapl}")
print(f"Gold variance: {var_gld}")

# Weight values for portfolio
w_aapl = .9
w_gld = 1- w_aapl
exp_aapl = .14
exp_gld = .07

# Expected return for portfolio
exp = (w_aapl * exp_aapl) + (w_gld * exp_gld)
print(f"Expected return: {exp}")

# Covariance calculation
cov = np.cov(change['AAPL'][1:], change['GLD'][1:])[0,1] * 252
print(f"Covariance: {cov}")

# Portfolio standard deviation
port_std = np.sqrt(var_aapl * w_aapl ** 2 + var_gld * w_gld ** 2 * cov * w_aapl * w_gld)
print(f"Portfolio Standard Deviation: {port_std}")

# Efficient frontier table (weight of apple, expected return, standard deviation)
effic = pd.DataFrame({'weight_aapl':np.zeros(21), 'exp_ret': np.zeros(21), 'std': np.zeros(21)})
w_aapl = 0.0
for weight in range(21):
    effic['weight_aapl'][weight] = w_aapl
    effic['exp_ret'][weight] = w_aapl * exp_aapl + (1-w_aapl) * exp_gld
    effic['std'][weight] = np.sqrt(var_aapl * w_aapl ** 2 + var_gld * (1-w_aapl) ** 2 + cov * w_aapl * (1 - w_aapl))
    w_aapl = w_aapl + .05

# Create coefficient frontier graph
with plt.style.context('seaborn'):
    plt.scatter(effic['std'], effic['exp_ret'])
    plt.title('Efficient Frontier')
    plt.ylabel('Expected Return')
    plt.xlabel('Standard Deviation')
    plt.savefig('efficient_frontier.png', bbox_inches='tight')