# -*- coding: utf-8 -*-
"""
Created on Wed May 24 08:21:20 2017

@author: Lafungo
"""

import datetime
from math import factorial

start = datetime.datetime.now()

def dfs(n):
    s = 0
    
    for d in str(n):
        s += factorial(int(d))
        
    return s

a = []
MAX = 10**6
c = 0

for n in range(2540160 + 1):
    a.append(dfs(n))

# Would be more efficient if already known values were marked
# and not checked repeatedly
for n in range(1, MAX + 1):
    seen = set()
    m = n
    
    while m not in seen:
        seen.add(m)
        m = a[m]
        
    if len(seen) == 60:
        c += 1
        
print(c)

end = datetime.datetime.now()
print(end - start)
