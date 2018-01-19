# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 08:28:48 2017

@author: Lafungo
"""

from sympy.ntheory import prevprime
import datetime

start = datetime.datetime.now()

def cycle(n):
    done = False
    r = 1
    val = []
    
    while not done:
        while r < n and r != 0:
            r *= 10
        
        r = r % n
        
        if r not in val:
            val.append(r)
        else:
            ind = val.index(r)
            val = val[ind:]
            done = True
            
    return val

d = 0
l = 0
MAX = 1000
p = prevprime(MAX)

while True:
    if p <= l:
        break
    
    p_cycle = cycle(p)
    pl = len(p_cycle)
    
    if pl > l:
        d = p
        l = pl
    
    p = prevprime(p)

print(d)

end = datetime.datetime.now()
print(end - start)
