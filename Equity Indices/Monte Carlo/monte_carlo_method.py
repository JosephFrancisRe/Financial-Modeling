# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 03:16:19 2023

@author: JosephRe
"""

import numpy.random as npr

# IRA account with ETF in S&P500
pv = 100000
er = 0.095
time_horizon = 30
ending_balance = 0

# Deterministic Method
print("{:10s} {:15s}".format("Year", "Ending Balance"))
print("-" * 26)
for year in range(1, time_horizon + 1):
    ending_balance = pv * (1 + er)
    print("{:<10d} {:15,.0f}".format(year, ending_balance))
    pv = ending_balance
    
# Add in volatility to incorporate randomness
market_volatility = .107
inflation = .038
volatility = market_volatility + inflation

# Reset starting balances
pv = 100000
er = 0.095
time_horizon = 30
ending_balance = 0

# Incorporate volatility assuming normal distribution
print("{:10s}  {:15s}".format("Year", "Ending Balance"))
print("-" * 26)
for year in range(1, time_horizon + 1):
    year_return = npr.normal(er, volatility)
    ending_balance = pv * (1 + year_return)
    print("{:<10d} {:>15,.0f}".format(year, ending_balance))
    pv = ending_balance