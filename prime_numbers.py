# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 10:11:11 2019

@author: milk
"""

i=2
while i<101:
    j=2
    while j<i:
        if i%j==0:
            break
        j+=1
    else:
        print(i)
    i+=1
