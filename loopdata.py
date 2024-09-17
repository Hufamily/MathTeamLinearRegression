# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 12:12:58 2024

@author: Ethan Hu
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

data=np.genfromtxt('loopdata.txt',delimiter = ',')
x,y=data.T
plt.close('all')
plt.plot(x,y,'ro')
plt.xlabel('x')
plt.ylabel('y')
def func(p,x,y):
    theta = np.arctan2(y,x)
    r=p
    return y-r*np.sin(theta)

fit = op.leastsq(func, x0=1, args=(x,y), full_output=1)
theta = np.linspace(0,2*np.pi,200)
xp = fit[0]*np.cos(theta)
yp = fit[0]*np.sin(theta)
error = np.sqrt(np.diag(fit[1])*np.var(func(fit[0],x,y),ddof=2))
plt.plot(xp, yp,'b-')
plt.text(-1,0,'$x^2+y^2=%s^2$'%str(fit[0]))