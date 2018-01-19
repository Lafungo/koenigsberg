# -*- coding: utf-8 -*-
"""
Created on Tue May 23 09:03:02 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import primerange, primepi
from math import sqrt, floor

start = datetime.datetime.now()

c = 0
MAX = 10**8

for p1 in primerange(1, floor(sqrt(MAX)) + 1):
    c += primepi(MAX // p1) - primepi(p1 - 1)
        
print(c)

end = datetime.datetime.now()
print(end - start)
