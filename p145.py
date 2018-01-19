# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:14:06 2017

@author: Lafungo
"""

import datetime

start = datetime.datetime.now()

# Bad brute-force approach which takes way too long

def r(n):
    return int(str(n)[::-1])

MAX = 10**9
c = 0

for n in range(11, MAX + 1):
    if n % 10 != 0:
        reversible = True
        m = n + r(n)
        
        for d in str(m):
            if int(d) % 2 == 0:
                reversible = False
                break
        
        if reversible:
            c += 1
            
print(c)

end = datetime.datetime.now()
print(end - start)
