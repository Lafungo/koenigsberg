# -*- coding: utf-8 -*-
"""
Created on Mon May  8 16:49:23 2017

@author: Lafungo
"""

import datetime
from math import sqrt

start = datetime.datetime.now()

MAX = 1000
triples = []
count = dict()

for n in range(1, MAX + 1):
    count[n] = 0
    
for n in range(1, MAX // 2):
    for m in range(n, MAX // 2):
        s = sqrt(n**2 + m**2)
        p = n + m + s
        
        if p > MAX:
            break
        
        if s == int(s):
            count[p] += 1

m_p = max(count, key=lambda k: count[k])
print(m_p)

end = datetime.datetime.now()
print(end - start)
