# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 10:06:58 2024

@author: Ethan Hu
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
plt.close('all')
k1=0.9
k2=0.9
k3 = 0.9
l1 = 1
l2 = 1
l3 = 1
m1 = 3
m2 = 3
def dx_dt(t, X):
    x1,x2,dx1,dx2 = X #Create vy, the velocity of y or the first derivative
    global k1
    global k2
    global k3
    global l1
    global l2
    global l3
    global m1
    global m2
    return [dx1,dx2,(-k1*x1 - 2.0*k2*x1 + 2.0*k2*x2 - l1*dx1 - l2*dx1)/m1, (2.0*k2*x1 - 2.0*k2*x2 - k3*x2 - l2*dx2 - l3*dx2)/m2]
t = np.arange(0,100,.001)#T = 2pi/omega

result = integrate.solve_ivp(dx_dt,(0,100),y0=(2,2,-1,1),max_step=.01,t_eval=t,method='LSODA')
print(result.y,'\n'+result.message)
x1,x2,v1,v2 = result.y
plt.plot(t,x1,'r-', label='x1')
plt.plot(t,x2,'b-', label = 'x2')
#plt.plot(t,v1,'b-', label = 'velocity1')
#plt.plot(t,v2,'b-', label = 'velocity2')
plt.legend()
plt.xlabel('t')