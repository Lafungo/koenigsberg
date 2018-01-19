# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:14:57 2017

@author: Lafungo
"""

import datetime

start = datetime.datetime.now()

def r_max(a):
    m = a // 2
    
    if a % 2 == 0:
        r = 2 * (m - 1) * a
    else:
        r = (a - 1) * a
    
    return r

s = 0

for a in range(3, 1000 + 1):
    s += r_max(a)
    
print(s)

end = datetime.datetime.now()
print(end - start)
