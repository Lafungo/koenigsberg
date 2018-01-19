# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 08:23:05 2017

@author: Lafungo
"""

import datetime
from sympy.ntheory import nextprime, isprime

start = datetime.datetime.now()

p = 11
trunc = []

while len(trunc) < 11:
    sp = str(p)
    
    if (sp[0] in ('2', '3', '5', '7')) \
            and (sp[-1] in ('2', '3', '5', '7')):
        trunc_prime = True
                
        for i in range(1, len(sp)):
            if (len(sp[:i]) > 1 and len(sp[i:]) > 1) \
                    and (int(sp[:i]) % 2 == 0) or (int(sp[i:]) % 2 == 0):
                trunc_prime = False
                break
            elif not (isprime(int(sp[:i])) and isprime(int(sp[i:]))):
                trunc_prime = False
                break
        
        if trunc_prime:
            trunc.append(p)
    
    p = nextprime(p)

print(trunc)
print(sum(trunc))

end = datetime.datetime.now()
print(end - start)
