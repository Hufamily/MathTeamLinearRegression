# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 12:37:30 2024

@author: Ethan Hu
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as op

data = np.genfromtxt('polydata.txt', delimiter = ',')
x,y = data.T
plt.close('all')
plt.plot(x,y,'ro')
plt.ylabel('y')
plt.xlabel('x')

popt, pcov = np.polyfit(x,y,deg=2,cov=True)
err2 = np.sqrt(np.diag(pcov))

quad = np.poly1d(popt)
a,b,c = np.round(popt,3)
plt.plot(x,quad(x),'b-')
label = str(a)+'$x^2$+'+str(b)+'x+'+str(c)
plt.text(2.5, -300, label)
"""
popt, pcov = np.polyfit(x,y,deg=4,cov=True)
err4 = np.sqrt(np.diag(pcov))

quart = np.poly1d(popt)
plt.plot(x,quart(x),'g-')
"""
