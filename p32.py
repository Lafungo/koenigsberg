# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:45:48 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import divisors
from math import sqrt

start = datetime.datetime.now()

s = 0

def is_pan(n):
    s_n = str(n)
    
    if len(s_n) != 9:
        return False
    
    digits = []
    
    for digit in s_n:
        if digit == '0' or digit in digits:
            return False
        
        digits.append(digit)
        
    return True

for n in range(1000, 10000):
    div = divisors(n)
    
    for d in div:
        if d >= sqrt(n):
            break
        
        a = ''
        a += str(d) + str(n // d) + str(n)
        
        if is_pan(a):
            s += n
            break
        
print(s)

end = datetime.datetime.now()
print(end - start)
