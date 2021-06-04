# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 12:31:25 2019

@author: milk
"""

import numpy as np
A=np.array([1,2,3,4,5,6,7,8,9])
B=np.array([1,2,3,4,5,6,7,8,9])
for i in range(0,len(A)+1):
    for j in range(0,len(B)):
        print(A[i],'x',B[j],'=',A[i]*B[j],'\t',end="")
    print("\n")
        