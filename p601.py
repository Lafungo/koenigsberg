# -*- coding: utf-8 -*-
"""
Created on Wed May  3 10:14:38 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import primerange

start = datetime.datetime.now()

def P(s, N):
    c = 0
    m = 1
    
    for p in primerange(1, s + 1):
        i = 0
        
        while p**(i + 1) <= s:
            i += 1
            
        m *= p**i
    
    n = m + 1
    
    while n < N:
        if n % (s + 1) != 1:
            c += 1
            
        n += m
            
    return c

a = 0

for i in range(32):
    a += P(i, 4**i)

print(a)

end = datetime.datetime.now()
print(end - start)
