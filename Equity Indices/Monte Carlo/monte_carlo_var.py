# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 03:36:21 2023

@author: JosephRe
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as pdr
from scipy.stats import norm

# Ignores expected return as the time horizon is one month (or 21 business days)
# Deterministic calculation
CL = 0.95
TRADING_DAYS = 252
portfolio_val = 760000
volatility = 0.307
t = 21
cutoff = norm.ppf(CL)
VaR = portfolio_val * volatility * np.sqrt(t/TRADING_DAYS) * cutoff

print("At {:.2f} confidence level, loss will not exceed {:,.2f}".format(CL, VaR))
print("This represents a move of {:.2f} standard deviations below the expected return".format(cutoff))

# Probabilistic calculation
aapl = 5000
aapl_price = pdr.get_quote_yahoo('AAPL')['price']
aapl_value = aapl * aapl_price
aapl_value = aapl_value.at['AAPL']
t = 21/252
er = .19
volatility = .307
iterations = 50000
print(aapl_price)

# Monte Carlo Simulation value at risk - Black-Scholes pricing method for options
def VaR(pv, er, vol, T, iterations):
    end = pv * np.exp((er - .5 * vol ** 2) * T + 
                     vol * np.sqrt(T) * np.random.standard_normal(iterations))
    ending_values = end - pv
    return ending_values
at_risk = VaR(aapl_value,er,volatility, t, iterations)

plt.hist(at_risk,bins=50)
plt.title('Monte Carlo Value at Risk')
plt.ylabel('Number of Simulations Conducted')
plt.xlabel('Portfolio Losses and Gains ($USD)')
plt.savefig('monte_carlo_var.png', bbox_inches='tight')

percentiles = [1,5,10]
print(np.percentile(at_risk, percentiles))

print(aapl_price * 5000)