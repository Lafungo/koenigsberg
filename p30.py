# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:33:56 2017

@author: Lafungo
"""

import datetime

start = datetime.datetime.now()

def power_sum_digits(n, p):
    s = 0
    
    while n:
        s += (n % 10) ** p
        n //= 10
    
    return s

num = []

for n in range(2, 354294):
    if power_sum_digits(n, 5) == n:
        num.append(n)

print(sum(num))

end = datetime.datetime.now()
print(end - start)
