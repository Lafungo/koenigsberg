# -*- coding: utf-8 -*-
"""
Created on Tue May  9 10:42:36 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import isprime, primerange
from math import sqrt

start = datetime.datetime.now()

found = False
n = 9

while not found:
    n += 2
    found = True
    
    if not isprime(n):
        for p in primerange(1, n):
            m = sqrt((n - p) / 2)
            if m == int(m):
                found = False
    else:
        found = False

print(n)

end = datetime.datetime.now()
print(end - start)
