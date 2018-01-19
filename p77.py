# -*- coding: utf-8 -*-
"""
Created on Thu May 11 14:06:03 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import primerange

start = datetime.datetime.now()

def coins_comb(n, coins, max_coin):
    if n < 0 or max_coin < 0:
        return 0
    
    if n == 0 or max_coin == 0:
        return 1
    
    s = 0
    
    for m in range(n // coins[max_coin] + 1):
        s += coins_comb(n - (m * coins[max_coin]), coins, max_coin - 1)
    
    return s

n = 3
primes = [2]

while coins_comb(n, primes, len(primes) - 1) <= 5000:
    n += 1
    primes = [p for p in primerange(1, n)]

print(n)

end = datetime.datetime.now()
print(end - start)
