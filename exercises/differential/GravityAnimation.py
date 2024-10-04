from sympy import*
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import scipy.integrate as integrate
import matplotlib.patches as patches
x, y = symbols('x y')
U = -1/((x**2+y**2)**0.5)
Px = -diff(U, x)
Py = -diff(U, y)
print(Px)
print(Py)

dx = lambdify((x,y),Px)
dy = lambdify((x,y),Py)
def F(x,y):
    return [dx(x,y),dy(x,y)]

print(F(1,1))

X,Y=np.mgrid[-2:2:.1,-2:2:.1]
delta = 0.1
X,Y=X[np.sqrt(X**2+Y**2)>4*delta], Y[np.sqrt(X**2+Y**2)>4*delta]
U,V = F(X,Y)

#plt.quiver(X,Y,U,V, pivot='tail', units='xy', width=.0022, scale=7)

def ddt(t, X):
    x,dx,y,dy = X
    ddx, ddy = F(x,y)
    return [dx,ddx,dy,ddy]

t = np.arange(0,25,.001)
a=[.5,0,0,-.5]
result = integrate.solve_ivp(ddt,(0,25),y0=(a),max_step=.01,t_eval=t,method='LSODA')
x,vx,y,vy = result.y
#plt.plot(x,y,'r-')

fig = plt.figure()
ax = plt.axes(xlim = (-2,2),ylim = (-2,2))
ax.quiver(X,Y,U,V, pivot='tail', units='xy', width=.0022, scale=7)
line, = ax.plot([],[],'ro',lw=2)
#patch = patches.Arrow(a[0], a[1], a[2], a[3])
#ax.add_patch(patch)

def init():
    line.set_data([a[0]],[a[1]])
    #return line, patch,
    return line,
def animate(i):
    line.set_data([x[i]],[y[i]])
    #global patch
    #patch.remove()
    #patch = patches.Arrow(x[i], y[i], dx[i], dy[i])
    #ax.add_patch(patch)
    #return line, patch,
    return line,
anim = animation.FuncAnimation(fig,animate,init_func=init,frames = 25000,interval = 2, blit=True)