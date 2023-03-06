# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 23:27:03 2023

@author: JosephRe
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from statsmodels.tsa.holtwinters import SimpleExpSmoothing as ses

# Downloads gold info from yahoo finance, rounds values to 2 decimal places, and resamples the data as a weekly format
original_data = yf.download('GLD', start='2013-01-01', end='2019-01-06')
original_data = round(original_data, 2)
data = original_data.resample('W').last()

# Build the Simple Exponential Smoothing model
model = ses(data['Close'])
model_fit = model.fit()
y_hat = model_fit.fittedvalues

# Calculate changes in MSE as the alpha value is increased in the smoothing formula
values = pd.DataFrame({'alpha': np.zeros(10), 'MSE': np.zeros(10)})
alpha = 0.1
for i in range(10):
    model = ses(data['Close'])
    data['Forecast'] = model.fit(alpha).fittedvalues
    data['MSE'] = (data['Close'] - data['Forecast']) ** 2
    mse = data['MSE'].mean()
    values['alpha'][i] = alpha
    values['MSE'][i] = mse
    alpha += 0.1
print(values)

# Plots data
plt.title('Exponential Smoothing Forecast for Gold')
plt.ylabel('Close Price (USD)')
plt.xlabel('Time (Years)')
plt.plot(original_data.Close, label='Actual Close')
plt.plot(y_hat, label='Smoothed Close')
plt.legend(loc=1)
plt.savefig('gold_exponential_smoothing_forecast.png', box_inches='tight')