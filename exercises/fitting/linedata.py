# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:26:12 2024

@author: Ethan Hu
"""
import numpy as np
import matplotlib.pyplot as plt
path = "linedata.txt"
data = np.genfromtxt(path,delimiter = ',')
#x, y = np.split(data,[-1],axis=1)
x,y = data.T #Transpose the matrix
plt.close('all')
plt.plot(x, y, 'ro')
plt.xlabel('x')
plt.ylabel('y')

popt, pcov = np.polyfit(x,y,deg=1,cov=True)
err = np.sqrt(np.diag(pcov))#sqrt of diagonal elements of pcov are error

popt=np.round(popt,3)#rounds popt to three digits
m,b = popt
#plt.plot(x,m*x+b, 'b-')
func = np.poly1d(popt)


plt.plot(x,func(x), 'b-')
label = str(m)+'x+'+str(b) #Can use latex in python
plt.text(.5, 12.5,label)
#plt.text(.5, 12.5,str(func).split('\n')[1])#There is a \n at the beginning, so equation is on second line, error on third
