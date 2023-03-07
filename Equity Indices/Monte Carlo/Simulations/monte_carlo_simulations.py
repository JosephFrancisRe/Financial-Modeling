# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 03:27:38 2023

@author: JosephRe
"""

import numpy as np
import numpy.random as npr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

seaborn.set()
exp_return = .095
sd = .185
horizon = 30
iterations = 50000
starting = 100000
ending = 0

returns = np.zeros((iterations, horizon))
for t in range(iterations):
    for year in range(horizon):
        returns[t][year] = npr.normal(exp_return, sd)
returns[10000]

portfolio = np.zeros((iterations,horizon))
for iteration in range(iterations):
    starting = 100000
    for year in range(horizon):
        ending = starting * (1 + returns[iteration,year])
        portfolio[iteration,year] = ending
        starting = ending
        
portfolio = pd.DataFrame(portfolio).T
print(portfolio[list(range(5))])
print(portfolio.iloc[29].describe())

ending = portfolio.iloc[29]
mask = ending < 10000000
plt.figure(figsize=(12,8))
plt.xlim(ending[mask].min(), ending[mask].max() )
plt.hist(ending[mask], bins=100, edgecolor='k')
plt.axvline(ending[mask].median(), color='r')
plt.title('Monte Carlo Simulations')
plt.ylabel('Number of Simulations Conducted')
plt.xlabel('Portfolio Value ($USD)')
plt.savefig('monte_carlo_simulations.png', bbox_inches='tight')

percentiles = [1,5,10]
print(np.percentile(ending, percentiles))