# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:42:15 2018

@author: aver14
"""

inp = map(float,raw_input().split())

x,y = inp[0],inp[1]
res = 0.0

if x % 5 == 0:
    if y - 0.5 >= x:
        res = y - x - 0.5
        print "%.2f" % res
    else:
        print "%.2f" % y
else:
    print "%.2f" % y