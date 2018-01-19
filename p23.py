# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:46:03 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import divisors

start = datetime.datetime.now()

a = []
t = set()
s = []

for i in range(1, 28123 + 1):
    if (sum(divisors(i)) - i) > i:
        a.append(i)
        
for n in a:
    for m in a:
        t.add(n + m)

for n in range(1, 28123 + 1):
    if n not in t:
        s.append(n)
    
print(sum(s))
        
end = datetime.datetime.now()
print(end - start)
