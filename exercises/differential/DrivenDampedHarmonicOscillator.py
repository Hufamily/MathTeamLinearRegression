# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:59:37 2024

@author: Ethan Hu
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
plt.close('all')
K=100
b=10
m=3
def dx_dt(t, X):
    y, vy = X #Create vy, the velocity of y or the first derivative
    global K
    global b
    global m
    F=1#Iniial F at 0, .3
    omega = np.sqrt(33)#sqrtK
    return np.array([vy, (-K*y-b*vy+F*np.sin(omega * t))/m])#Return an array of all their derivatives
t = np.arange(0,20,.001)#T = 2pi/omega

result = integrate.solve_ivp(dx_dt,(0,20),y0=(0,.3),max_step=.01,t_eval=t,method='LSODA')
print(result.y,'\n'+result.message)
y,vy = result.y
plt.plot(t,y,'r-', label='position')
plt.plot(t,vy,'b-', label = 'velocity')
plt.legend()
plt.xlabel('t')