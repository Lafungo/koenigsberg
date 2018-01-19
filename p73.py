# -*- coding: utf-8 -*-
"""
Created on Mon May 15 11:32:49 2017

@author: Lafungo
"""

import datetime
from math import ceil

start = datetime.datetime.now()

f = set()
MAX = 12000

for d in range(5, MAX + 1):
    for n in range(ceil(d/3), ceil(d/2)):
        frac = n/d
        
        f.add(frac)

if 1/3 in f:
    f.remove(1/3)
    
if 1/2 in f:
    f.remove(1/2)

print(len(f))

end = datetime.datetime.now()
print(end - start)
