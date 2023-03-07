# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 15:49:42 2023

@author: JosephRe
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('sp500_1950_mon.csv')

plt.title('S&P500 Adjusted Close Price Since 1950')
plt.ylabel('Adjusted Close Price')
plt.xlabel('Months')
plt.plot(data['Adj Close'])
plt.savefig('sp500_close_price_1950_thru_2018.png', bbox_inches='tight')