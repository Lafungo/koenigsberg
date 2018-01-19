# -*- coding: utf-8 -*-
"""
Created on Tue May  9 13:16:35 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import divisors

start = datetime.datetime.now()

MAX = 10**6

frac = dict()
frac[1] = 0
s = 0

for n in range(2, MAX + 1):
    c = n - 1
    
    for d in divisors(n)[:-1]:
        c -= frac[d]
        
    frac[n] = c
    s += c

print(s)

end = datetime.datetime.now()
print(end - start)
