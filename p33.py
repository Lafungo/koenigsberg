# -*- coding: utf-8 -*-
"""
Created on Mon May  8 16:05:21 2017

@author: Lafungo
"""

import datetime
from math import gcd

start = datetime.datetime.now()

a = []

for n in range(10, 99):
    for m in range(n + 1, 100):
        if n % 10 == 0:
            break
        
        if m % 10 != 0:
            f = n / m
            n1 = n // 10
            n2 = n % 10
            m1 = m // 10
            m2 = m % 10
            
            if n2 == m2 and n1 / m1 == f:
                a.append((n, m))
            elif n2 == m1 and n1 / m2 == f:
                a.append((n, m))
            elif n1 == m2 and n2 / m1 == f:
                a.append((n, m))
            elif n1 == m1 and n2 / m2 == f:
                a.append((n, m))
                
num = 1
den = 1

for (n, m) in a:
    num *= n
    den *= m
    
print(den // gcd(num, den))

end = datetime.datetime.now()
print(end - start)
