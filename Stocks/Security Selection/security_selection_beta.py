# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 23:07:54 2023

@author: JosephRe
"""

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as lr

# Define index and stocks to be put into a regression
stocks = ['^GSPC', 'AAPL']

# Create a dataframe and populate it with close values.
data = pd.DataFrame()
count = 0
for stock in stocks:
    value = yf.download(stock, start='2018-02-01')['Close']
    data.insert(count, column=stock, value=value)
    count += 1
    
# Resample data to use the last business day in the month
data = data.resample('BM').last()

# Drop the observation for March 2023 data as this is prematurely populated
data = data[:data.shape[0]-1]

print(data)

# Create dataframe with the natural log change
change = pd.DataFrame()
for column in data:
    if column not in change:
        change[column] = np.log(data[column]).diff()
change = change.dropna()

print(change)

# Create and fit linear regression model
model = lr(fit_intercept=True)
x = np.array(change['^GSPC'])
y = np.array(change['AAPL'])
model.fit(x[:, np.newaxis], y)
xfit = np.linspace(x.min(), x.max(), 100)
yfit = model.predict(xfit[:, np.newaxis])

# Calculate linear regression line of best fit equation
m = round(model.coef_[0], 3)
b = round(model.intercept_, 3)
line = 'y=' + str(m) + 'x' + ('+' if (b>=0) else '-') + str(abs(b))

# Create plot
plt.scatter(x,y,label='DataPoints')
plt.plot(xfit, yfit, c='r', label=line)
plt.title('Linear Regression of AAPL vs. S&P500')
plt.ylabel('Log Difference in % (AAPL)')
plt.xlabel('Log Difference in % (S&P500)')
plt.legend(loc=2)
plt.savefig('aapl_beta_linear_regression.png', bbox_inches='tight')

# Extract beta value from the slope of the linear regression's line of best fit
beta = model.coef_
print(f"AAPL's beta is {beta}")

# Calculate beta value manually
cov = np.cov(change['AAPL'], change['^GSPC'], ddof=1)
beta = cov[0,1] / cov[1,1]
print(f"AAPL's beta is {beta}")