# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 09:10:28 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import primefactors

start = datetime.datetime.now()

found = False
n = 1

while not found:
    consec = 0
    
    for i in range(4):
        if len(primefactors(n + i)) != 4:
            n += i + 1
            break
        
        consec += 1
        
    if consec == 4:
        found = True

print(n)

end = datetime.datetime.now()
print(end - start)
