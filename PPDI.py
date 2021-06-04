# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 09:37:22 2019

@author: milk
"""
for i in range(100,501):
    a=(i//100)**3
    b=((i%100)//10)**3
    c=((i-a*100)%10)**3
    if i==a+b+c:
        print(i)
        