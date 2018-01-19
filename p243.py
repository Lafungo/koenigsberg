# -*- coding: utf-8 -*-
"""
Created on Fri May 12 13:01:18 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import totient, nextprime

start = datetime.datetime.now()

def R(n):
    return totient(n) / (n - 1)

stop = 15499 / 94744
n = 2
p = 2

while R(n) >= stop:
    p = nextprime(p)
    n *= p

n //= p

c = 2

while R(n * c) >= stop:
    c += 1

print(n * c)

end = datetime.datetime.now()
print(end - start)
