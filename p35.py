# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 14:11:58 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import primerange, isprime

start = datetime.datetime.now()

def rotate(i, n):
    l = str(i)
    l = l[n:] + l[:n]
    return int(l)

circle = []

for p in primerange(1, 10 ** 6):
    circular = True
    
    for n in range(1, len(str(p))):
        if not isprime(rotate(p, n)):
            circular = False
            
    if circular:
        circle.append(p)
        
print(circle)

end = datetime.datetime.now()
print(end - start)
