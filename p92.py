# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:41:36 2017

@author: Lafungo
"""

"""
Brute-force approach, inefficient.
Can be made faster by pre-computing for 1 - 567,
since dssum can return at most 9^2 * 7 = 567.
"""

import datetime

start = datetime.datetime.now()

def dssum(n):
    s = 0
    
    while n:
        s += (n % 10) ** 2
        n //= 10
    
    return s

count = 0

for n in range(2, 10 ** 7 + 1):
    c = n
    
    while c != 1 and c != 89:
        c = dssum(c)
    
    if c == 89:
        count += 1

print(count)

end = datetime.datetime.now()
print(end - start)
