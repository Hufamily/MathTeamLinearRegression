# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 12:03:34 2024

@author: Ethan Hu
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
plt.close('all')
def dx_dt(X, t, K):
    y, vy = X #Create vy, the velocity of y or the first derivative
    return np.array([vy, -K*y])#Return an array of all their derivatives
t = np.arange(0,2*np.pi/10,.001)#T = 2pi/omega

result = integrate.odeint(dx_dt, y0 =(30,0), t=t, args = (100,), full_output=True)
print(result[0].T,'\n'+result[-1]['message'])
y,vy = result[0].T
plt.plot(t,y,'r-', label='position')
plt.plot(t,vy,'b-', label = 'velocity')
plt.legend()