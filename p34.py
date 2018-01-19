# -*- coding: utf-8 -*-
"""
Created on Thu May  4 12:12:10 2017

@author: Lafungo
"""

import datetime
from math import factorial

start = datetime.datetime.now()

MAX = 2540160
a = 0

for i in range(3, MAX):
    s = 0
    
    for digit in str(i):
        s += factorial(int(digit))
        
    if s == i:
        a += i
        
print(a)

end = datetime.datetime.now()
print(end - start)
