# -*- coding: utf-8 -*-
"""
Created on Thu May  4 13:05:40 2017

@author: Lafungo
"""

import datetime

start = datetime.datetime.now()

tri = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 
       171, 190, 210, 231, 253, 276, 300, 325, 351, 378]

f = open('p042_words.txt', 'r')
words = [word.strip('"') for word in f.read().split(',')]
num_words = [sum([ord(letter) % 32 for letter in word]) for word in words]

c = 0
for num in num_words:
    if num in tri:
        c += 1
        
print(c)

end = datetime.datetime.now()
print(end - start)
