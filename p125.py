# -*- coding: utf-8 -*-
"""
Created on Wed May 31 08:37:59 2017

@author: Lafungo
"""

import datetime

start = datetime.datetime.now()

def is_palin(n):
    return n == int(str(n)[::-1])

MAX = 10**8
n = 2
c = 0
s = 0
stop = False
sqs = set()

while not stop:
    i = 1
    j = n
    sq = sum([k**2 for k in range(1, j + 1)])
    
    while sq < MAX:
        sqs.add(sq)
        
        sq -= i**2
        i += 1
        j += 1
        sq += j**2
        
    if j == n:
        stop = True
        
    n += 1
        
for sq in sqs:
    if is_palin(sq):
        c += 1
        s += sq
        
print(str(c) + " palindromes summing to "  + str(s))

end = datetime.datetime.now()
print(end - start)
