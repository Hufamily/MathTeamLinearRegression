# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:18:32 2024

@author: Ethan Hu
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

data = np.genfromtxt('powerdata.txt',delimiter = ',')
x,y = data.T
plt.close('all')
plt.plot(x,y,'ro')
plt.xlabel('x')
plt.ylabel('y')

def func(x, a, b,c):
    return a*np.exp((b*x))+c
popt,pcov = op.curve_fit(func, x, y, p0 = (2,1,0), sigma = None, absolute_sigma = False, method ='lm')
error = np.sqrt(np.diag(pcov))
a,b,c = popt
plt.plot(x,func(x,a,b,c),'b-')
popt=np.round(popt,3)
a,b,c = popt
label = str(a)+'$e^{%s x}$'%str(b)+str(c)
plt.text(.5, 45,label)
