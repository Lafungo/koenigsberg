# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:31:41 2017

@author: Lafungo
"""

"""
Brute-force solution. Very inefficient.
"""
sum = 0

for i in range(1001):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
        
print(sum)

"""
Better solution.
"""
def count(n, s):
    ceil = n // s
    val = (ceil * (ceil + 1)) / 2
    return int(s * val)

sum = count(1000, 3) + count(1000, 5) - count(1000, 3 * 5)

print(sum)
