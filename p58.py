# -*- coding: utf-8 -*-
"""
Created on Mon May 15 11:08:57 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import isprime

start = datetime.datetime.now()

c = 3
t = 5
n = 1

while (c / t) >= .1:
    if isprime(4 * n**2 + 6 * n + 3):
        c += 1
        
    if isprime(4 * n**2 + 8 * n + 5):
        c += 1
        
    if isprime(4 * n**2 + 10 * n + 7):
        c += 1
        
    n += 1
    t += 4
        
print(2 * n + 1)

end = datetime.datetime.now()
print(end - start)
