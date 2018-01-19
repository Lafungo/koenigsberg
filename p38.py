# -*- coding: utf-8 -*-
"""
Created on Mon May  8 16:24:02 2017

@author: Lafungo
"""

import datetime

start = datetime.datetime.now()

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

m = 0

for n in range(9000, 10000):
    a = ''
    a += str(n) + str(2*n)
    
    if is_pan(a):
        m = a
        
print(m)

end = datetime.datetime.now()
print(end - start)
