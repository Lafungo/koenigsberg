# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:58:17 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import isprime, primepi, prime, primerange

start = datetime.datetime.now()

MAX = 10 ** 6

# check sums of length i
for i in range(1, primepi(MAX)):
    if sum(primerange(1, prime(i) + 1)) > MAX:
        break
    
    # start sum at integer j
    for j in primerange(1, prime(primepi(MAX - (i - 1)) + 1)):
        l = list(primerange(j, prime(primepi(j) + (i - 1)) + 1))
        sl = sum(l)
        
        if sl >= MAX:
            break
        
        if isprime(sl):
            s = i
            p = sl
            break
    
print(s)
print(p)

end = datetime.datetime.now()
print(end - start)
