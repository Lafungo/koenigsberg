# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 12:04:47 2017

@author: Lafungo
"""

"""
Brute-force approach that doesn't terminate in any reasonable amount of time

Only non-trivial step is that g(n) = sum of g(i), where i is a divisor of n
(i != n)
"""
from sympy.ntheory import divisors
import datetime

start = datetime.datetime.now()

MAX = 10**5
sum = 0
chain_count = dict()
chain_count[1] = 1

for i in range(2, MAX + 1):
    goz = 0
    
    for j in divisors(i):
        if j != i:
            goz += chain_count[j]
    
    chain_count[i] = goz
    
    if goz == i:
        sum += goz
        
print(sum)
end = datetime.datetime.now()
print(end - start)
