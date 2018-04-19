# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 12:10:09 2018

@author: aver14
"""

inp = map(int,raw_input().split())

n,k = inp[0],inp[1]
count = 0

for i in range(0,n):
    t = int(raw_input())
    if t % k == 0:
        count = count + 1
        
print count