# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:31:50 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import primefactors, multiplicity

start = datetime.datetime.now()

# Awfully slow brute-force

def s(n):
    pf = primefactors(n)
    r = 0
    
    for p in pf:
        mult = multiplicity(p, n)
        m = 0
        c = 0
        
        if p * mult > r:
            while c < mult:
                m += 1
                c += multiplicity(p, m) + 1
                
            mp = m * p
            
            if mp > r:
                r = mp
    
    return r

def S(n):
    r = 0
    
    for n in range(2, n + 1):
        r += s(n)
    
    return r

print(S(10**8))

end = datetime.datetime.now()
print(end - start)
