# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 22:24:16 2023

@author: JosephRe
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

def fv(pv, r, T):
    return round(pv * (1+r)**T, 2)

def print_fv(fv):
    import locale
    locale.setlocale(locale.LC_ALL, '')
    print(locale.currency(fv, grouping=True))

pv = random.randrange(10000, 100001)
r = random.randrange(50, 101) / 10000
T = 1
fv = fv(pv, r, T)
print_fv(fv)