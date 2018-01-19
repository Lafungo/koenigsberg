# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:10:39 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import primerange, isprime

start = datetime.datetime.now()

def q_prime(a, b):
    n = 0
 
    while isprime(n**2 + (a * n) + b):
        n += 1
    
    return n

MAX = 1000
max_chain = 0

for b in primerange(0, MAX):
    for a in range(MAX):
        q = q_prime(a, b)
        if q > max_chain:
            max_chain = q
            max_a = a
            max_b = b
        else:
            q = q_prime(-a, b)
            if q > max_chain:
                max_chain = q
                max_a = -a
                max_b = b

print(max_a, max_b, max_chain)
print(max_a * max_b)

end = datetime.datetime.now()
print(end - start)
