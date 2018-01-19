# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:05:08 2017

@author: Lafungo
"""

MIN = 1000000000
MAX = 1414213563

for num in range(MIN, MAX + 1, 10):
    square = num ** 2
    
    if (square % 1000) // 100 == 9 and (square % 10 ** 5) // 10 ** 4 == 8 \
        and (square % 10 ** 7) // 10 ** 6 == 7 \
        and (square % 10 ** 9) // 10 ** 8 == 6 \
        and (square % 10 ** 11) // 10 ** 10 == 5 \
        and (square % 10 ** 13) // 10 ** 12 == 4 \
        and (square % 10 ** 15) // 10 ** 14 == 3 \
        and (square % 10 ** 17) // 10 ** 16 == 2:
        value = square
        break

print(num)
