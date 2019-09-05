import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from numpy.linalg import inv
from math import sin

## Example1
c = np.linspace(-3,3,7)
x = np.linspace(-5,5,101)

print(c)

def y_sin(x):
	return np.sin(x)

def dy_cos(x):
	return np.cos(x)

for i in range(len(c)):
	f = y(x) + c[i]
	plt.plot(x,f)
plt.show()

############################
# Example_2
# air_drag

t = np.linspace(0,5,11)
v0 = np.linspace(0,50,11)

gravity = 9.8
air_drag = 0.47
arrow_len = 0.5

u_array =[]
v_array =[]

for i in range(len(t)):
	for j in range(len(v0)):
		dv = gravity - (air_drag*v0[j])
		u = np.cos(np.arctan(dv))*arrow_len
		v = np.sin(np.arctan(dv))*arrow_len
		u_array.append(u)
		v_array.append(v)
		# plt.quiver([t[i],v0[j]],u,v,'k')

X,Y = np.meshgrid(t,v0)
u_array = np.array(u_array)
v_array = np.array(v_array)
u1 = np.reshape(u_array,(11,11))
v1 = np.reshape(v_array,(11,11))

plt.quiver(Y,X,u1,v1)
plt.show()

########################
### Example 3
### Eulers method

x0 = 0
y0 = 1

x = np.linspace(0,2,21)
y = lambda x: np.exp(-x)

plt.figure()
plt.plot(x,y(x),'k','LineWidth',2)
# plt.show()

deltax = 0.4
xvec = np.linspace(x0,x[-1],((x[-1]-x0)/deltax)+1)
yvec = []
yvec.append(y0)

for i in range(len(xvec)):
	yvec.append(yvec[i] + (-yvec[i])*deltax)
	plt.plot(xvec[i],yvec[i],'o')#,'MarkerFaceColor','b','MarkerEdgeColor','k')

plt.show()

########################
### Runga_Kutle method

def dydx(x,y):
	return -y

def RK4(x0,y0,h):
	# n = (int)((x-x0)/h)
	k1 = h*dydx(x0,y0)
	k2 = h*dydx(x0+h/2, y0+k1/2)
	k3 = h*dydx(x0+h/2, y0+k2/2)
	ky = h*dydx(x0+h, y0+k3/2)

	yn = y0 + (k1+ 2*k2 + 2*k3 + ky)/6
	
	return yn

x0 = 0
y0 = 1

x = np.linspace(0,2,21)
y = lambda x: np.exp(-x)

plt.figure()
plt.plot(x,y(x),'k','LineWidth',2)

deltax = 0.4
xvec = np.linspace(x0,x[-1],((x[-1]-x0)/deltax)+1)
yvec = []
yvec.append(y0)

for i in range(len(xvec)):
	yvec.append(RK4(xvec[i],yvec[i],deltax))
	plt.plot(xvec[i],yvec[i],'o')

plt.show()

##################
### assignment_4

### assignment_4a
### (x**2 + y**2)
def dydx(x,y):
	return (x**2 + y**2)

def RK4(x0,y0,h):
	# n = (int)((x-x0)/h)
	k1 = h*dydx(x0,y0)
	k2 = h*dydx(x0+h/2, y0+k1/2)
	k3 = h*dydx(x0+h/2, y0+k2/2)
	ky = h*dydx(x0+h, y0+k3/2)

	yn = y0 + (k1+ 2*k2 + 2*k3 + ky)/6
	
	return yn

x0 = 0
y0 = 1

x = np.linspace(0,2,21)

plt.figure()

deltax = 0.04
xvec = np.linspace(x0,x[-1],((x[-1]-x0)/deltax)+1)
yvec = []
yvec.append(y0)

for i in range(len(xvec)):
	yvec.append(RK4(xvec[i],yvec[i],deltax))
	plt.plot(xvec[i],yvec[i],'o')#,'MarkerFaceColor','b','MarkerEdgeColor','k')

plt.show()

### assignment_4b
###(x*y)

def dydx(x,y):
	return (x*y)

def RK4(x0,y0,h):
	k1 = h*dydx(x0,y0)
	k2 = h*dydx(x0+h/2, y0+k1/2)
	k3 = h*dydx(x0+h/2, y0+k2/2)
	ky = h*dydx(x0+h, y0+k3/2)

	yn = y0 + (k1+ 2*k2 + 2*k3 + ky)/6
	
	return yn

x0 = 0
y0 = 1

x = np.linspace(0,2,21)

plt.figure()

deltax = 0.04
xvec = np.linspace(x0,x[-1],((x[-1]-x0)/deltax)+1)
yvec = []
yvec.append(y0)

for i in range(len(xvec)):
	yvec.append(RK4(xvec[i],yvec[i],deltax))
	plt.plot(xvec[i],yvec[i],'o')#,'MarkerFaceColor','b','MarkerEdgeColor','k')

plt.show()

###################################