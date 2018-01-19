# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 11:43:10 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import totient, primefactors

start = datetime.datetime.now()

def rad(n):
    r = 1
    
    for p in primefactors(n):
        r *= p
        
    return r

def is_perm(n, m):
    sn = str(n)
    sm = str(m)
    
    if len(sn) != len(sm):
        return False
    
    return sorted(sn) == sorted(sm)

MAX = 10**7
n = 0
q = MAX

# Inefficient, better would be to search for product of large primes first

for m in range(3, MAX, 2):
    t = totient(m)
    r = m / t
    
    if r < q and is_perm(t, m):
        n = m
        q = r
        
print(n, q)

end = datetime.datetime.now()
print(end - start)
