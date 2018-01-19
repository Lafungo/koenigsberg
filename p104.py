# -*- coding: utf-8 -*-
"""
Created on Mon May 15 14:25:21 2017

@author: Lafungo
"""

import datetime
from sympy import fibonacci

start = datetime.datetime.now()

def is_pan(n):
    sn = str(n)
    
    d = set([str(x) for x in range(1, len(sn) + 1)])
    
    return set(sn) == d

n = 102
l1 = int(str(fibonacci(100))[-9:])
l2 = int(str(fibonacci(101))[-9:])
c = l1 + l2
found = False

while not found:
    n += 1
    l1 = l2 % 10**9
    l2 = c % 10**9
    c = (l1 + l2) % 10**9
    
    if is_pan(c):
        b = str(fibonacci(n))[:9]
        
        if is_pan(b):
            found = True
            
print(n)

end = datetime.datetime.now()
print(end - start)
