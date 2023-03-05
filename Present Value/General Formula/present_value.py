# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 21:23:48 2023

@author: JosephRe
"""

import random
import locale

def pv(FV, r, T):
    return FV / (1+r)**T

def display_result(value):
    locale.setlocale(locale.LC_ALL, '')    
    print(locale.currency(PV, grouping=True))

random.seed()
FV = random.randrange(10000, 100001)
r = random.randrange(30, 70, 5) / 1000
T = random.randrange(1, 30)
PV = pv(FV, r, T)
display_result(PV)