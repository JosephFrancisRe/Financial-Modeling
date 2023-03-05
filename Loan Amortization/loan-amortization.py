# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 13:43:09 2023

@author: JosephRe
"""

import numpy as np
import numpy_financial as npf
import pandas as pd
import matplotlib.pyplot as plt

# Initial Inputs
pv = 360000
rate = 0.05875
term = 30

# Calculate monthly payment
pmt = npf.pmt(rate / 12, term * 12, -pv)

# Create structure of amortization table
amort_table = pd.DataFrame({'Balance': np.zeros(term * 12 + 1),
                            'Interest': np.zeros(term * 12 + 1),
                            'Principal': np.zeros(term * 12 + 1),
                            'Cum_Int.': np.zeros(term * 12 + 1)})

# Populate first row of amortization table
amort_table['Balance'][0] = pv
amort_table['Interest'][0] = amort_table['Balance'][0] * rate / 12
amort_table['Principal'][0] = pmt - amort_table['Interest'][0]
amort_table['Cum_Int'] = amort_table['Interest'].cumsum()

# Populate remainder of amortization table and round results
for row in range(1,360):
    amort_table['Balance'][row] = amort_table['Balance'][row - 1] - amort_table['Principal'][row - 1]
    amort_table['Interest'][row] = amort_table['Balance'][row] * rate / 12
    amort_table['Principal'][row] = pmt - amort_table['Interest'][row]
amort_table['Cum_Int'] = amort_table['Interest'].cumsum()
amort_table = round(amort_table, 2)

# Plot Balance against Cum_Int
with plt.style.context('ggplot'):
    plt.title('Loan Amortization (Balance v. Cum_Int)')
    plt.xlabel('Payment Number in Months')
    plt.ylabel('Value in USD')
    plt.plot(amort_table['Balance'], label='Balance')
    plt.plot(amort_table['Cum_Int'], label='Cum_Int')
    plt.legend(loc=5)
    plt.savefig('loan_amort_bal_vs_cum_int.png', bbox_inches='tight')
    