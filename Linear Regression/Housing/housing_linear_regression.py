# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 05:40:20 2023

@author: JosephRe
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as lr

# Read in .csv file and remove any columns that contain at least one na value
housing = pd.read_csv('housing.csv')
housing.dropna(inplace=True)

# Generate correlation matrix to verify a strong positive correlation
housing[['Price (00s)', 'SqFt']].corr()

# Create model, fit it to sqft and price, and create a string representing the
# line equation for the least squares regression line
model = lr(fit_intercept=True)
price = np.array(housing['Price (00s)'])
sqft = np.array(housing['SqFt'])
model.fit(sqft[:, np.newaxis], price)
m = round(model.coef_[0], 2)
b = round(model.intercept_, 2)
line = 'y=' + str(m) + 'x' + ('+' if (b>=0) else '-') + str(abs(b))
xfit = np.linspace(sqft.min(), sqft.max(), 100)
yfit = model.predict(xfit[:, np.newaxis])

# Create scatter plot containing linear regression line
plt.scatter(price, sqft, label='DataPoints')
plt.plot(yfit, xfit, c='r', label=line)
plt.title('Price by SqFt (with least squares regression line)')
plt.ylabel('Price (USD)')
plt.xlabel('Square Footage')
plt.legend(loc=2)
plt.savefig('housing_linear_regression.png', bbox_inches='tight')