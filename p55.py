# -*- coding: utf-8 -*-
"""
Created on Fri May 12 10:03:49 2017

@author: Lafungo
"""

import datetime

start = datetime.datetime.now()

def is_pan(n):
    return str(n) == str(n)[::-1]

def l_step(n):
    return n + int(str(n)[::-1])

MAX = 10**4
c = 0

for n in range(1, MAX + 1):
    m = l_step(n)
    
    for i in range(50):
        if is_pan(m):
            c += 1
            break
        
        m = l_step(m)
        
print(MAX - c)

end = datetime.datetime.now()
print(end - start)
