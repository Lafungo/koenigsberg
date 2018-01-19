# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 13:33:06 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import divisors, isprime

start = datetime.datetime.now()

def dr(n):
    s = str(n)
    t = n
    
    while len(s) > 1:
        t = 0
        
        for d in s:
            t += int(d)
            
        s = str(t)
        
    return t

def mdrs(n):
    if n == 1:
        return 0
    
    if isprime(n):
        return dr(n)
    
    m = max([mdrs(d) + mdrs(n//d) for d in divisors(n)[1:-1]])
    
    return max(m, dr(n))

def smdrs(n):
    a = []
    
    for k in range(n):
        a.append(0)
        
    for k in range(2, n):
        if isprime(k):
            a[k] = dr(k)
        else:
            a[k] = max(max([a[d] + a[k//d] for d in divisors(k)[1:-1]]), dr(k))
        
    return sum(a)

print(smdrs(10**6))

end = datetime.datetime.now()
print(end - start)
