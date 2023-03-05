# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 15:06:39 2023

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
extra_principal = 100

def amortize(pv, rate, term, extra_principal=0):
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
        actual_pmt = pmt + extra_principal
        amort_table['Balance'][row] = max(0, 
            amort_table['Balance'][row - 1] - amort_table['Principal'][row - 1])
        amort_table['Interest'][row] = amort_table['Balance'][row] * rate / 12
        amort_table['Principal'][row] = actual_pmt - amort_table['Interest'][row]
        if amort_table['Balance'][row] < actual_pmt:
            amort_table['Principal'][row] = amort_table['Balance'][row]
            break
    amort_table = amort_table[amort_table['Balance'] != 0]
    amort_table['Cum_Int'] = amort_table['Interest'].cumsum()
    amort_table = round(amort_table,2)
    summary = pd.Series({
        'Interest': rate,
        'Payment' : round(pmt,2),
        'Extra Principal' : extra_principal,
        'Total Interest' : amort_table['Cum_Int'].max(),
        'Periods' : amort_table.index[-1] + 1
    })    
    
    return amort_table, summary

def plot_scenario_analysis(scenario_1, scenario_2, scenario_3):
    with plt.style.context('ggplot'):
        plt.title('Loan Amortization Scenario Analysis')
        plt.xlabel('Periods (Months)')
        plt.ylabel('Balance ($USD)')
        plt.plot(scenario_1['Balance'], label='Scenario 1')
        plt.plot(scenario_2['Balance'], label='Scenario 2')
        plt.plot(scenario_3['Balance'], label='Scenario 3')
        plt.legend(loc=1)
        plt.savefig('loan_amortization_scenario_analysis.png', bbox_inches='tight')

amort_table, summary = amortize(pv, rate, term)

scenario_1, summary_1 = amortize(pv, rate, term, 100)
scenario_2, summary_2 = amortize(pv, rate, term, 200)
scenario_3, summary_3 = amortize(pv, .0475, 15)

scenario_analysis = pd.DataFrame([summary_1, summary_2, summary_3])
scenario_analysis = scenario_analysis.rename(index={0:'Scenario 1', 1:'Scenario 2', 2:'Scenario 3'})
plot_scenario_analysis(scenario_1, scenario_2, scenario_3)
print(scenario_analysis)