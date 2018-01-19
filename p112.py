# -*- coding: utf-8 -*-
"""
Created on Tue May  9 13:02:40 2017

@author: Lafungo
"""

import datetime

start = datetime.datetime.now()

c = 99
n = 99

while c / n != .01:
    n += 1
    s_n = str(n)
    sort_s_n = sorted(s_n)
    
    if sort_s_n == list(s_n) or list(reversed(sort_s_n)) == list(s_n):
        c += 1
        
print(n)

end = datetime.datetime.now()
print(end - start)
