# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 21:48:53 2023

@author: JosephRe
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import locale

def discount_payments(num_of_payments, r):
    for T in range(num_of_payments):
        cashflows[T] = round(cashflows[T] / (1+r)**T, 2)

def plot(cashflows):
    fig = plt.figure()
    plt.plot(cashflows)
    plt.grid(linestyle='--')
    plt.xticks([0,5,10,15,20])
    plt.title('Present Value of Lottery Payments Over Time')
    plt.xlabel('Time in Years')
    plt.ylabel('Present Value in USD')
    fig.savefig('lottery_pv_over_time.png', bbox_inches='tight')
    
def discounted_payments_pv(cashflows):
    return sum(cashflows)

def print_discounted_payments_pv(cashflows):
    locale.setlocale(locale.LC_ALL, '')
    print(locale.currency(discounted_payments_pv(cashflows), grouping=True))

r = 0.05
cashflows = np.ones(20) * random.randrange(10000, 100001)
num_of_payments = cashflows.size
discount_payments(num_of_payments, r)
print_discounted_payments_pv(cashflows)
plot(cashflows)