# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:02:02 2024

@author: Ethan Hu
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
#plt.close('all')

plt.figure()

plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Populations Without Lampreys')

Lamprey = 10 #Red
PrimaryPrey = 25 #Blue
SecondaryPrey = 20000 #Green
Larva = [10,10,10,10,10,10]
#Larva = [0,0,0,0,0,0]
i=0
a = 0.001
b = .001
c = 1
M = 50
timeStop = 0
K = 100000
plt.plot(0,Lamprey,'r-', label = 'Lamprey')
plt.plot(0,PrimaryPrey,'b-', label = 'Primary Prey')
plt.plot(0,SecondaryPrey,'g-', label = 'Secondary Prey')
def phaseA(t,X):
    L, PP, SP, H, H1 = X
    dL = -a * L
    if dL>0:
        dL=0
    dL = dL + 0.1*H - b*L
    dPP = -0.75*PP + 0.0004*SP*PP - 0.1*L*(0.02*PP)/(1+0.02*PP)
    dSP = 0.1*SP*(1-SP/K)-0.004*SP*PP
    if H > 0:
        dH = -0.1*H
    else:
        H=0
        dH=0
    dH1 = b*(L)*(100-M)/100*1000

    return [dL,dPP,dSP,dH,dH1]


def phaseB(t,X):
    L, PP, SP, H = X
    dL = -a * L + 0.1*L*(0.02*PP)/(1+0.02*PP)
    if dL>0:
        dL=0
    dL = dL + 0.1*H
    dPP = -0.75*PP + 0.0004*SP*PP - 0.1*L*(0.02*PP)/(1+0.02*PP)
    dSP = 0.1*SP*(1-SP/K)-0.004*SP*PP
    if H > 0:
        dH = -0.1*H
    else:
        H=0
        dH=0

    return [dL,dPP,dSP,dH]

def func(x, a, b,c,d):
    return a*np.exp(b*(x-d))+c

index = np.arange(0,30)
PP = []
SP = []
L = []
Resource = [270.97, 287.27, 305.92, 305.85, 315.22, 333.21, 349.4, 337.72, 369.65, 377.79]
for j in index:
    t = np.arange(0,3,.03)
    
    result = integrate.solve_ivp(phaseA,(0,3),y0=(Lamprey,PrimaryPrey,SecondaryPrey,Larva[i],Larva[(i+1)%6]),max_step=.01,t_eval=t,method='LSODA')
    t = t+timeStop
    plt.plot(t,result.y[0],'r-')
    plt.plot(t,result.y[1],'b-')
    plt.plot(t,result.y[2],'g-')
    timeStop+=3
    L = np.append(L, result.y[0])
    PP = np.append(PP, result.y[1])
    SP = np.append(SP, result.y[2])
    Lamprey = result.y[0][-1]
    PrimaryPrey = result.y[1][-1]
    SecondaryPrey = result.y[2][-1]
    Larva[i] = result.y[4][-1]
    i = (i+1)%6
    
    M = func(Resource[j%len(Resource)],109.697,  -0.703,  38.701,  23.228)
    D = (100-M)*0.01
    Larva[i] = (1-D)*Larva[i]
    if Larva[i]<0:
        Larva[i] = 0
    t = np.arange(0,9,.03)
    result = integrate.solve_ivp(phaseB,(0,9),y0=(Lamprey,PrimaryPrey,SecondaryPrey,Larva[i]),max_step=.01,t_eval=t,method='LSODA')
    t= t+timeStop
    timeStop+=9
    plt.plot(t,result.y[0],'r-')
    plt.plot(t,result.y[1],'b-')
    plt.plot(t,result.y[2],'g-')
    L = np.append(L, result.y[0])
    PP = np.append(PP, result.y[1])
    SP = np.append(SP, result.y[2])
    Lamprey = result.y[0][-1]
    PrimaryPrey = result.y[1][-1]
    SecondaryPrey = result.y[2][-1]
    Larva[i] = result.y[3][-1]

plt.legend()
plt.figure()
plt.plot(PP, SP, 'ro')
plt.xlabel('Primary Prey')
plt.ylabel('Secondary Prey')
plt.title('Predator Prey without Lamprey')

from mpl_toolkits import mplot3d
 
fig = plt.figure()
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')
 
# defining all 3 axis
z = L
x = PP
y = SP
 
# plotting
ax.plot3D(x, y, z, 'green')
ax.set_title('Relationship between 3 Populations')
plt.show()