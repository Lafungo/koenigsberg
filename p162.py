# -*- coding: utf-8 -*-
"""
Created on Thu May  4 16:55:11 2017

@author: Lafungo

Note: incorrect
"""

import datetime
from sympy import binomial

start = datetime.datetime.now()

MAX = 16
s = 4

for i in range(4, MAX + 1):
    s += 2 * 2 * binomial(i - 1, 2) * (16 ** (i - 3)) \
        + 13 * 6 * binomial(i - 1, 3) * (16 ** (i - 4))
        
print(s)
print(hex(s))

end = datetime.datetime.now()
print(end - start)
