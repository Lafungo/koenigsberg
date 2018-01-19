# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:32:54 2017

@author: Lafungo
"""

f = open('p022_names.txt', 'r')

names = sorted([word.strip('"') for word in f.read().split(',')])
rank = 1
count = 0

for name in names:
    value = 0
    
    for letter in name:
        value += ord(letter) - 64
        
    value *= rank
    count += value
    
    rank += 1

print(count)
