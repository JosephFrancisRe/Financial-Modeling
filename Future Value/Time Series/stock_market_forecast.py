# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 23:08:51 2023

@author: JosephRe

Numbers are based on estimates from the S&P 500
"""

import numpy as np
import matplotlib.pyplot as plt

def randomize_market_price_fluctation(market_price):
    for T in range(len(market_price)):
        r = np.random.normal(0.1188, 0.15)
        if T > 0:
            market_price[T] = round(market_price[T - 1] * (1 + r))
        else:
            market_price[T] = market_price[T]

def plot_market_price(y):
    x = np.arange(0, len(y), 1)
    fig = plt.scatter(x, y, color = 'blue', label = 'Data Points')
    fit = np.polyfit(x, y, 2)
    a = fit[0]
    b = fit[1]
    c = fit[2]
    fit_eq = a*np.square(x) + b*x + c
    plt.plot(x, fit_eq, color = 'red', alpha = 0.5, label = "Polynomial Fit")
    plt.title('Market Price Over Time')
    plt.xlabel('Time in Years')
    plt.ylabel('Market Price in USD')
    plt.grid(linestyle='--')
    plt.xticks([0,5,10,15,20])
    plt.legend(loc = 2)
    fig.figure.savefig('market_price_over_time.png', bbox_inches='tight')

market_price = np.ones(20) * 50000
randomize_market_price_fluctation(market_price)
print(market_price)
plot_market_price(market_price)