# -*- coding: utf-8 -*-
"""
Created on Wed May 10 08:12:27 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import totient

start = datetime.datetime.now()

MAX = 10**6
m = 0
t = 0

for n in range(1, MAX + 1):
    r = n / totient(n)
    
    if r > t:
        m = n
        t = r
        
print(m)        

end = datetime.datetime.now()
print(end - start)
