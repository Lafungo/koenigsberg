# -*- coding: utf-8 -*-
"""
Created on Tue May  9 08:11:09 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import prevprime

start = datetime.datetime.now()

def is_pan(n):
    s_n = str(n)
    
    if set(s_n) == set(['1', '2', '3', '4', '5', '6', '7']):
        return True
    else:
        return False
    
#    if len(s_n) != 9:
#        return False
    
#    digits = []
#    
#    for digit in s_n:
#        if digit == '0' or digit in digits:
#            return False
#        
#        digits.append(digit)
#        
#    return True

found = False
p = prevprime(10**7)

while not found:
    if is_pan(p):
        pan_prime = p
        found = True
        
    p = prevprime(p)

print(pan_prime)

end = datetime.datetime.now()
print(end - start)
