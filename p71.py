# -*- coding: utf-8 -*-
"""
Created on Mon May 15 11:50:23 2017

@author: Lafungo
"""

import datetime
from math import gcd

start = datetime.datetime.now()

MAX = 10**6

def reduce(a, b):
    d = gcd(a, b)
    
    return (a//d, b//d)

p = 2
q = 5

while q <= MAX:
    (a, b) = (p, q)
    (p, q) = reduce(p + 3, q + 7)

print(a)

end = datetime.datetime.now()
print(end - start)
