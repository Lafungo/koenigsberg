# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 13:11:01 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import divisors

start = datetime.datetime.now()

def dsum(n):
    s = 0
    
    for d in divisors(n, generator=True):
        s += d
        
    return s - n

MAX = 10**6
m = 0
a = 0

for n in range(1, MAX + 1):
    chain = set()
    chain.add(n)
    ds = dsum(n)
    
    while True:
        if ds < n or ds in chain or ds > MAX:
            break
        
        chain.add(ds)
        ds = dsum(ds)
            
    c = len(chain)
    
    if c > m and ds == n:
        m = c
        a = min(chain)
        
print(m, a)

end = datetime.datetime.now()
print(end - start)
