# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 22:40:07 2023

@author: JosephRe
"""

import numpy as np
import matplotlib.pyplot as plt

def calc_future_balances(ending_balance):
    for T in range(1, len(ending_balance)):
        ending_balance[T] = round(ending_balance[T] * (1+r)**T, 2)

def plot_balances(ending_balance):
    fig = plt.figure()
    plt.plot(ending_balance)
    plt.xticks([0,5,10,15,20])
    plt.grid(linestyle="--")
    plt.title('Ending Balance Over Time')
    plt.xlabel('Time in Years')
    plt.ylabel('Balance in USD')
    fig.savefig('ending_balance_over_time.png')

r = 0.05
ending_balance = np.ones(20) * 100000
calc_future_balances(ending_balance)
plot_balances(ending_balance)