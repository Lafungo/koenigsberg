# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:30:28 2017

@author: Lafungo
"""

import datetime

start = datetime.datetime.now()

matrix = []

f = open('p081_matrix.txt', 'r')
for line in f:
    matrix.append([int(n) for n in list(line.split(sep=','))])
f.close()

for i in range(1, len(matrix[0])):
    matrix[0][i] += matrix[0][i - 1]

for j in range(1, len(matrix)):
    matrix[j][0] += matrix[j - 1][0]
    
for i in range(1, len(matrix[0])):
    for j in range(1, len(matrix)):
        matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])
         
print(matrix[len(matrix[0]) - 1][len(matrix) - 1])

end = datetime.datetime.now()
print(end - start)
