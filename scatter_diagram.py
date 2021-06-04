# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:01:48 2019

@author: milk
"""

import scipy.io as sio
import matplotlib.pyplot as plt
Data=sio.loadmat('moon.mat')
coordinate=Data['moon'][:]
x=coordinate[:,0]
y=coordinate[:,1]
a=0
for i in range(len(x)):
   a=a+x[i]
avx=a/len(x)
b=0
for i in range(len(y)):
   b=b+y[i]
avy=b/len(y)
all=0
for i in range(len(x)):
    c=x[i]-avx
    d=y[i]-avy
    all=all+c*d
e=0
for i in range(len(x)):
    e=e+(x[i]-avx)**2
beta=all/e
sigma=avy-avx*beta
y1=beta*x+sigma
plt.plot(x,y,'ob',label='moon')
plt.plot(x,y1,'r',label='y=beta*x+sigma')
plt.legend(loc='upper right')
plt.title("105011240")
plt.show