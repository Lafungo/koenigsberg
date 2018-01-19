# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:54:12 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import primerange

start = datetime.datetime.now()

s = set()

for p3 in primerange(1, 83 + 1):
    for p2 in primerange(1, 367 + 1):
        p23 = p2**3 + p3**4
        
        if p23 >= 5 * 10**7:
            break
        
        for p1 in primerange(1, 7069 + 1):
            p123 = p1**2 + p23
            
            if p123 >= 5 * 10**7:
                break
            
            s.add(p123)

print(len(s))

end = datetime.datetime.now()
print(end - start)
