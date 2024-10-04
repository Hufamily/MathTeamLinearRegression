# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:25:30 2024

@author: Ethan Hu
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
plt.close('all')
def dx_dt(X, t, A, B, C, D):
    x,y = X
    return np.array([A*x-C*x*y,-B*y+D*x*y])
t = np.arange(0,40,.1)

result = integrate.odeint(dx_dt, y0 =(10,10), t=t, args = (1.5,.3,.6,.3), full_output=True)
print(result[0].T,'\n'+result[-1]['message'])
X, Y = np.mgrid[0:10:.1,0:10:.1]
U, V = dx_dt((X,Y),0,1.5,.3,.6,.3)
plt.quiver(X,Y,U,V,pivot='tail',angles='xy',units='xy',width=.0022,scale=7)
x,y = result[0].T
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y,'r-')

plt.figure()
plt.xlabel('t')
plt.ylabel('x')
plt.plot(t,x,'r-')

plt.figure()
plt.xlabel('t')
plt.ylabel('y')
plt.plot(t,y,'r-')
