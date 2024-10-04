# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 12:08:19 2024

@author: Ethan Hu
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

path = 'sinedata.txt'
data = np.genfromtxt(path, delimiter = ',')
x,y = data.T
plt.close('all')
plt.plot(x,y,'ro')

def func(x,a,b,c,d):
    return a*np.sin(b*x+c)+d

popt, pcov = op.curve_fit(func, x, y, p0=(10,6, 0,0), sigma = None, absolute_sigma = False, method='lm')
a,b,c,d = popt
error = np.sqrt(np.diag(pcov))
plt.plot(x,func(x, a, b, c, d),'b-')
#Could do func(x,*popt), * pops out the array
popt = np.round(popt,3)
a,b,c,d = popt
label = str(a)+'sin('+str(b)+'x+'+str(c)+')+'+str(c)
plt.text(1.0, 0.2, label)
