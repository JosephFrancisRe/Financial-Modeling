# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 01:32:34 2023

@author: JosephRe
"""

import numpy as np
import numpy_financial as npf

# Input values and cashflow vector
initial_investment = 1000000
years = np.arange(1,6)
cashflows = np.ones(5) * 300000
irr_cashflows = [-initial_investment, 300000, 300000, 300000, 300000, 300000]
cost_of_capital = npf.irr(irr_cashflows)

# Vectorized numpy math operation to discount cashflows
discounted_cashflows = cashflows / (1 + cost_of_capital) ** years

# IRR calculation
irr = initial_investment - sum(discounted_cashflows)

# Print Operations
print(f"IRR = {irr}")
if round(irr, 5) == 0:
    print("The IRR calculation given flexibility for root approximation worked correctly.", end = '')
else:
    print("The IRR calculating did not work as expected.", end = '')
