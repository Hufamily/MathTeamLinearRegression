# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:37:11 2024

@author: Ethan Hu
"""

import numpy as np
import scipy.optimize as op
import matplotlib.pyplot as plt

data = np.genfromtxt('semidata.txt', delimiter = ',')
x,y = data.T
plt.close('all')
plt.plot(x,y,'ro')
plt.ylabel('y')
plt.xlabel('x')
plt.yscale('log')
def func(x,a,b,c,d):
    return a*np.exp(b*x+c)+d

popt,pcov = op.curve_fit(func,x,y,p0=(1,-1,3,10),sigma=None,absolute_sigma=False,method='lm')
error = np.sqrt(np.diag(pcov))
plt.plot(x,func(x,*popt),'b-')
a,b,c,d=np.round(popt,3)
label = str(a)+'$e^{%s}$+'%(str(b)+'x+'+str(c))+str(d)
plt.text(7,1,label)