# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:23:45 2024

@author: Ethan Hu
"""
import numpy as np
import matplotlib.pyplot as plt

"""
dx = .01
x = np.arange(0,10,dx)
one = np.ones(x.size-1)
D = (np.diag(one,1)-np.diag(one,-1))/(2*dx) #Diagonals are numbered, this matrix assumes f(0) is 0, since it's f_n(x)-f_n-1(x)
y=x**2*np.exp(-4*(x-5)**2)
plt.plot(x,y,'r.',x,D.dot(y),'b-')#Red line is original equation, D.dot(y) takes dot product between the derivative matrix and y, giving derivative

D2 = D.dot(D)#Second derivative [-2,0,1;0-2,0,1;] => Is laplacian(Second derivative) with additional diagonals
"""

dx = .01
x = np.arange(0,10,dx)
one = np.ones(x.size-1)
two = 2*np.ones(x.size)
D = (np.diag(one,1)-np.diag(one,-1))/(2*dx)
D2 = (-np.diag(two,0)+np.diag(one,-1)+np.diag(one,1))/(dx**2)
y = x**2*np.exp(-4*(x-5)**2)
plt.plot(x,y,'r.',x,D.dot(y),'b-',x,D.dot(D.dot(y)),'go',x,D2.dot(y),'g-')