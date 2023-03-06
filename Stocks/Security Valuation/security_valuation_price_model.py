# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 02:45:15 2023

@author: JosephRe
"""

import numpy as np
import pandas as pd

def run_expected_return_model():
    # Expected return for fictitious stock
    div = 3.92
    p0 = 75.00
    p1 = 88.71
    er = (div + p1) / p0
    print('------Expected Return-----')
    print(f'Expected return: {er - 1}')
    
    pv = (div + p1) / er
    print(f'Current value: {pv}')


def run_dividend_discount_model():
    # Dividend Discount Model
    g = .08
    er = .12
    p1 = 81
    div = 3
    
    horizon = pd.DataFrame({'div': np.zeros(3), 'exp_price': np.zeros(3)})
    horizon.index = np.arange(1, len(horizon) + 1)
    horizon.index.name = 'Year'
    
    for T in range(1, len(horizon) + 1):
        if T == 1:
            horizon['div'][T] = div
            horizon['exp_price'][T] = p1
        else:
            horizon['div'][T] = div * (1 + g) ** (T - 1)
            horizon['exp_price'][T] = p1 * (1 + g) ** (T - 1)
    
    price = round((horizon['div'][1] + horizon['exp_price'][1]) / (1 + er), 2)
    print(f'Dividend Discount Model Price: {price}')
    return price


def run_constant_growth_model():
    # Constant Growth Model
    div = 3
    g = .08
    er = .12
    
    price = round(div / (er - g), 2)
    print(f"Constant Growth Model Price: {price}")
    return price


def run_pe_model():
    # Price to Earnings (PE) Model
    eps = 5.60
    pe = 15
    er = .12
    
    price = round(eps * pe / (1 + er), 2)
    print(f"PE Model: {price}")
    return price


# Run Expected Return Calc
run_expected_return_model()
print('\n----------Models----------')

# Run Models
p1 = run_dividend_discount_model()
p2 = run_constant_growth_model()
p3 = run_pe_model()
print('\n----------Results----------')

if (p1 == p2 == p3):
    print('All models produced the same security valuation.')
else:
    print('There is a discrepency in the security valuation across models.')