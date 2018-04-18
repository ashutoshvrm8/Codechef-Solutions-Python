# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:33:08 2018

@author: aver14
"""

t = int(raw_input());

while t != 0:
    inp = map(int,raw_input().split())
    
    flag = 0
    
    for i in range(0,t):
        if i+1 != inp[inp[i]-1]:
            flag = 1
            break;
            
    if flag == 1:
        print 'not ambiguous'
    else:
        print 'ambiguous'
    
    t = int(raw_input());