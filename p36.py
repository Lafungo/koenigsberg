# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:22:58 2017

@author: Lafungo
"""

import datetime

start = datetime.datetime.now()

dbp = []

for n in range(1, 10 ** 6, 2):
    sn = str(n)
    bn = format(n, 'b')
    
    if sn == sn[::-1] and bn == bn[::-1]:
        dbp.append(n)
    
print(dbp)
print(sum(dbp))

end = datetime.datetime.now()
print(end - start)
