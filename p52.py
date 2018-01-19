# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:05:55 2017

@author: Lafungo
"""

import datetime

start = datetime.datetime.now()

def is_perm(n, m):
    return sorted(str(n)) == sorted(str(m))

found = False
n = 1

while not found:
    if all(is_perm(n, m * n) for m in range(2, 7)):
        x = n
        found = True
        
    n += 1
        
print(x)

end = datetime.datetime.now()
print(end - start)
