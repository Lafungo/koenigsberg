# -*- coding: utf-8 -*-
"""
Created on Tue May 23 13:31:37 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import factorint
from sympy import lcm

start = datetime.datetime.now()

def carmichael(n):
    f = factorint(n)
    l = 1
    
    for p, k in f.items():
        if p == 2 and k > 2:
            l = lcm(l, 2**(k - 2))
        else:
            l = lcm(l, (p - 1) * p**(k - 1))
            
    return l

def carmichael_mods(n):
    m = [n]
    
    while n > 2:
        n = carmichael(n)
        m.append(int(n))
        
    return m

def hyper_mod(a, b, n):
    m = carmichael_mods(n)
    m = m[:min(len(m), b)]
    r = 1
    
    for k in reversed(m):
        r = pow(a, r, k)
        
    return r

print(hyper_mod(1777, 1855, 10**8))

end = datetime.datetime.now()
print(end - start)
