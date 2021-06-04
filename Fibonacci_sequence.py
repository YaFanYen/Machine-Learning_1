# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:30:06 2019

@author: milk
"""
import numpy as np
def f(x):
    F=[0,1]
    num=1
    for i in range(2,x+1):
        F=np.append(F,F[-1]+F[-2])
        num=num+F[i]**2
    print(num)
    return num
f(x=15)

