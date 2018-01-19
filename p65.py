# -*- coding: utf-8 -*-
"""
Created on Tue May 30 10:58:10 2017

@author: Lafungo
"""

import datetime
from fractions import Fraction

start = datetime.datetime.now()

def e_conv(n):
    if n == 1:
        return Fraction(2)
    if n == 2:
        return Fraction(3)
    
    if n % 3 == 0:
        return 

end = datetime.datetime.now()
print(end - start)
