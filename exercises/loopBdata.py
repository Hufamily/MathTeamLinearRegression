# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 07:59:09 2024

@author: Ethan Hu
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as op

data = np.genfromtxt('loopBdata.txt', delimiter = ',')
x,y = data.T
plt.close('all')
plt.plot(x,y,'ro')
plt.xlabel('x')
plt.ylabel('y')

def func(p,x,y):
    a,b,c,d = p
    theta = np.arctan2(a*(y-d),b*(x-c))
    return np.sqrt((x-(a*np.cos(theta)+c))**2+(y-(b*np.sin(theta)+d))**2)

fit = op.leastsq(func, x0=(2.1,1,2.5,-2.4), args=(x,y), full_output=1)
error = np.sqrt(np.diag(fit[1])*np.var(func(fit[0],x,y),ddof=2))
a,b,c,d = fit[0]
theta = np.linspace(0,2*np.pi,200)
xp = np.cos(theta)*a+c
yp = np.sin(theta)*b+d
plt.plot(xp,yp,'b-')
a,b,c,d = np.round(fit[0],3)
plt.text(0.8,-3,r'$(\frac{{x-%s}}{{%s}})^2+(\frac{{y-%s}}{{%s}})^2=1^2$'%(str(c),str(a),str(d),str(b)) )
"""
def func(p, x, y):
    a, b, c, d = p
    theta = np.arctan2(y-d,x-c)
    e= ((1-(b/a)**2))
    thetae = np.arctan2(np.sqrt(1-e)*np.sin(theta),np.sqrt(e)+np.cos(theta))
    #return np.sqrt((x-c)**2+(y-d)**2) - np.sqrt( (np.sin(thetae)*b+d)**2 + (np.cos(thetae)*a+c)**2 )
    return y-(np.sin(thetae)*b+d)

fit = op.leastsq(func, x0=(2.1,1,2.5,-2.4), args=(x,y), full_output=1)
error = np.sqrt(np.diag(fit[1])*np.var(func(fit[0],x,y),ddof=2))
theta = np.linspace(0,2*np.pi,200)
a, b, c, d = fit[0]
e=np.sqrt(1-(b/a)**2)
thetae = np.arctan2(np.sqrt(1-e**2)*np.sin(theta),e+np.cos(theta))
xp = np.cos(thetae)*a+c
yp = np.sin(thetae)*b+d
plt.plot(xp, yp,'b-')


plt.figure()
theta = np.arctan2(y-d,b)
e=np.sqrt(1-(b/a)**2)
thetae = np.arctan2(np.sqrt(1-e**2)*np.sin(theta),e+np.cos(theta))
r = np.sqrt( (np.sin(thetae)*b+d)**2 + (np.cos(thetae)*a-c)**2 )
plt.plot(theta, r,'bo')


r = np.sqrt((x-c)**2+(y-d)**2)
plt.plot(theta, r,'ro')


a,b,c,d = np.round(fit[0],3)
plt.text(3,-3,r'$(\frac{{x-%s}}{{%s}})^2+(\frac{{y-%s}}{{%s}})^2=1^2$'%(str(c),str(a),str(d),str(b)) )
"""