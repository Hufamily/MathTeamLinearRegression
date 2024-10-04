# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 12:02:38 2024

@author: Ethan Hu
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as op

data = np.genfromtxt('iGEMdata.txt',delimiter = ',')
x,y=data.T
plt.close('all')
plt.plot(x,y,'ro')
plt.ylabel('y')
plt.xlabel('x')
#plt.yscale('log')
def func(x,a,b,c,d):
    return a*np.exp(b*x+c)+d

popt,pcov = op.curve_fit(func,x,y,p0=(3,-1,3,3),sigma=None,absolute_sigma=False,method='lm')
error = np.sqrt(np.diag(pcov))
tx = np.linspace(0,80,200)
plt.plot(tx,func(tx,*popt),'b-')
a,b,c,d=np.round(popt,3)
label = str(a)+'$e^{%s}$+'%(str(b)+'x+'+str(c))+str(d)
plt.text(40,100,label)
