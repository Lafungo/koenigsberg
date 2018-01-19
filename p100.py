# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 10:19:14 2017

@author: Lafungo
"""

import datetime
from math import sqrt, floor, ceil

start = datetime.datetime.now()

# Top-down approach
n = 10 ** 9
found = False

def check(n):
    m = (n * (n - 1)) / 2
    sm = sqrt(m)
    
    if floor(sm) != ceil(sm) \
            and (m % floor(sm) == 0) and (m % ceil(sm) == 0):
        return True
    
while not found:
    n += 1

    if n % 4 == 2:
        n += 2

    if check(n):
        m = (n * (n - 1)) / 2
        sm = sqrt(m)
        found = True

print(ceil(sm))

end = datetime.datetime.now()
print(end - start)

# Summation approach
# Must be some way to reduce values of n and/or m to check
#def int_sum(n):
#    return (n * (n + 1)) // 2
#
#n = 10 ** 9
#ns = int_sum(n - 1)
#m = ceil(sqrt((n * (n - 1)) / 2))
#ms = int_sum(m - 1)
#found = False
#
#while not found:
#    ns += n
#    n += 1
#    
#    if n % 4 == 2:
#        ns += 2 * n + 1
#        n += 2
#        
##    for m in range(ceil((n - 1) / sqrt(2)), ceil(n / sqrt(2)) + 1):
##        ms = int_sum(m - 1)
##        
##        if 2 * ms == ns:
##            found = True
##            break
#    
#    while 2 * ms < ns:
#        ms += m
#        m += 1
#        
#    if 2 * ms == ns:
#        found = True
#        
#print(m)
#
#end = datetime.datetime.now()
#print(end - start)

# Bottom-up approach (appears to be slower than top-down)
#n = 70710678 #707106781186
#found = False
#
#while not found:
#    n += 1
#    
#    m = 2 * n * (n - 1)
#    sm = sqrt(m)
#    
#    if floor(sm) != ceil(sm) \
#            and (m % floor(sm) == 0) and (m % ceil(sm) == 0):
#        found = True
#
#print(n)
#
#end = datetime.datetime.now()
#print(end - start)