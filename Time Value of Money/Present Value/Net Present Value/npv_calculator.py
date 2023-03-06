# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 22:56:45 2023

@author: JosephRe
"""

import numpy as np
import locale

# Input values and cashflow vector
initial_investment = 1000000
cost_of_capital = 0.12
years = np.arange(1,6)
cashflows = np.ones(5) * 300000

# Vectorized numpy math operation to discount cashflows
discounted_cashflows = cashflows / (1 + cost_of_capital) ** years

# NPV calculation
npv = sum(discounted_cashflows) - initial_investment

# Print Operations
locale.setlocale(locale.LC_ALL, '')
print(f"NPV = {locale.currency(npv, grouping=True)}")
if npv > 0:
    print("This investment opportunity is worth pursuing.", end = '')
else:
    print("This investment is not worth pursuing as it does not generate income.", end = '')