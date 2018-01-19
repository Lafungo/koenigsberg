# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:03:37 2017

@author: Lafungo
"""

"""
Brute-force solution. Still fast for this instance of problem.
Amounts to calculating all previous values of Pascal's triangle.
"""

paths = dict()
paths[(0, 0)] = 1

for i in range(1, 20 + 1):
    paths[(i, 0)] = 1

for j in range(1, 20 + 1):
    paths[(0, j)] = 1

for i in range(1, 20 + 1):
    for j in range(1, 20 + 1):
        paths[(i, j)] = paths[(i - 1, j)] + paths[(i, j - 1)]

print(paths[(20, 20)])

"""
Compute value using direct formula for Pascal's triangle.
"""

from scipy.misc import comb

print(int(comb(40, 20)))
