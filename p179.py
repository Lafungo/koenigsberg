# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:55:24 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import divisors

start = datetime.datetime.now()

div = []
MAX = 10**7
c = 0

for n in range(MAX + 1):
    div.append(len(divisors(n)))

for i in range(1, len(div)):
    if div[i - 1] == div[i]:
        c += 1

print(c)

end = datetime.datetime.now()
print(end - start)
