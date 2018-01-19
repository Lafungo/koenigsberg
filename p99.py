# -*- coding: utf-8 -*-
"""
Created on Fri May 12 15:08:55 2017

@author: Lafungo
"""

import datetime
from math import log

start = datetime.datetime.now()

e = []

f = open('p099_base_exp.txt', 'r')
for line in f:
    e.append([int(n) for n in list(line.split(sep=','))])
f.close()

l = 0
m = 0

for i in range(len(e)):
    n = e[i][1] * log(e[i][0])
    
    if n > m:
        l = i + 1
        m = n
        
print(l)

end = datetime.datetime.now()
print(end - start)
