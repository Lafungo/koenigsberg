# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:29:46 2017

@author: Lafungo
"""

import datetime

start = datetime.datetime.now()

tri = []
t = 285
penta = []
p = 165
hexa = []
h = 143
found = False

while not found:
    t += 1
    p += 1
    h += 1
    
    tri.append((t * (t + 1)) / 2)
    penta.append((p * (3 * p - 1)) / 2)
    hexa.append(h * (2 * h - 1))
    
    if tri[-1] in penta and tri[-1] in hexa:
        found = True

print(tri[-1])

end = datetime.datetime.now()
print(end - start)
