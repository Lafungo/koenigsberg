# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:54:44 2017

@author: Lafungo
"""

import datetime

start = datetime.datetime.now()

def digit_sum(n):
    return sum([int(d) for d in str(n)])

m = 0

for a in range(1, 100):
    for b in range(1, 100):
        ds = digit_sum(a**b)
        
        if ds > m:
            m = ds
            
print(m)

end = datetime.datetime.now()
print(end - start)
