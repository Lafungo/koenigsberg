# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 15:34:24 2017

@author: Lafungo
"""

import datetime

start = datetime.datetime.now()

f = open('p067_triangle.txt', 'r')

numbers = []

for line in f:
    numbers.append(line.strip().split())

f.close()
    
for row in reversed(range(len(numbers) - 1)):
    for index in range(len(numbers[row])):
        numbers[row][index] = int(numbers[row][index]) + \
                                max([int(numbers[row + 1][index]), 
                                     int(numbers[row + 1][index + 1])]) 

print(numbers[0][0])

end = datetime.datetime.now()
print(end - start)
