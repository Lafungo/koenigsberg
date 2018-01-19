# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:05:25 2017

@author: Lafungo
"""

import datetime

start = datetime.datetime.now()

s = 0

for n in range(1, 10):
    p = 1
    
    while len(str(n**p)) == p:
        s += 1
        p += 1

print(s)

end = datetime.datetime.now()
print(end - start)
