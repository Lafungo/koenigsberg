# -*- coding: utf-8 -*-
"""
Created on Thu May 11 13:52:04 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import npartitions

start = datetime.datetime.now()

n = 1

while npartitions(n) % 10**6 != 0:
    n += 1
    
print(n)

end = datetime.datetime.now()
print(end - start)
