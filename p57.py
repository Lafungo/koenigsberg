# -*- coding: utf-8 -*-
"""
Created on Tue May 30 09:09:06 2017

@author: Lafungo
"""

import datetime
from fractions import Fraction

start = datetime.datetime.now()

MAX = 1000
c = 0
f = Fraction(3/2)

for n in range(2, MAX + 1):
    f = 1 + 1/(1 + f)
    
    if len(str(f.numerator)) > len(str(f.denominator)):
        c += 1
        
print(c)

end = datetime.datetime.now()
print(end - start)
