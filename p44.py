# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:46:41 2017

@author: Lafungo
"""

import datetime

start = datetime.datetime.now()

penta = []
n = 1
found = False

while not found:
    p = (n * (3 * n - 1)) // 2
    penta.append(p)
    n += 1
    
    for m in penta:
        if m >= p / 2:
            break
        
        k = p - m
        if k in penta:
            if k - m in penta:
                s = (m, k)
                found = True

print(s)
print(s[1] - s[0])

end = datetime.datetime.now()
print(end - start)
