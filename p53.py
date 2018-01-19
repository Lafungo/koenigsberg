# -*- coding: utf-8 -*-
"""
Created on Tue May  2 10:15:32 2017

@author: Lafungo
"""

import datetime
from sympy import binomial

start = datetime.datetime.now()

c = 0

for n in range(101):
    for r in range(n + 1):
        if binomial(n, r) > 10 ** 6:
            c += n + 1 - 2 * r
            break
            
print(c)

end = datetime.datetime.now()
print(end - start)
