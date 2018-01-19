# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:39:15 2017

@author: Lafungo
"""

from sympy.ntheory import divisors

MAX = 10000
count = 0

for num in range(1, MAX):
    am = sum(divisors(num)) - num
    
    if am != num and (sum(divisors(am)) - am) == num:
        count += num
        
print(count)
