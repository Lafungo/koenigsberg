# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:13:25 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import divisors, isprime, primerange
from math import sqrt

start = datetime.datetime.now()

def is_gen(n):
    gen = True
    
    for d in divisors(n):
        if not isprime(d + n//d):
            gen = False
            break
        
        if d > sqrt(n):
            break
        
    return gen

s = 0
MAX = 10**8

for p in primerange(1, MAX + 1):
    if isprime((p + 3) // 2):
        if is_gen(p - 1):
            s += p - 1
        
print(s)

end = datetime.datetime.now()
print(end - start)
