# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:38:22 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import primerange, isprime

start = datetime.datetime.now()

def is_perm(n, m):
    return sorted(str(n)) == sorted(str(m))

primes = []
s = []

for p in primerange(1000, 10000):
    primes.append(p)
    
for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        n, m = primes[i], primes[j]
        if is_perm(n, m):
            k = 2 * n - m
            if isprime(k) and is_perm(n, k):
                s.append((n, m, k))

print(s)

end = datetime.datetime.now()
print(end - start)
