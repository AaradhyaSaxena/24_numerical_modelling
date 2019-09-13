import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from numpy.linalg import inv
from math import sin

def dydx(x,y):
	return (-y/2)

x0 = 0
y0 = 1

x = np.linspace(0,2,21)

# plt.figure()

deltax = 0.04
xvec = np.linspace(x0,x[-1],((x[-1]-x0)/deltax)+1)
yvecEU = []
yvecEU_mod = []
yvecEU.append(y0)
yvecEU_mod.append(yvecEU[0] + dydx(xvec[0],yvecEU[0])*deltax)

for i in range(len(xvec)-1):
	yvecEU.append(yvecEU[i] + dydx(xvec[i],yvecEU[i])*deltax)
	yvecEU_mod.append(yvecEU_mod[i] + (dydx(xvec[i],yvecEU_mod[i]) + dydx(xvec[i+1],yvecEU[i+1]))*deltax)
	plt.plot(xvec[i],yvecEU[i], '.')
print(i)
plt.show()

##(y-x)

def dydx(x,y):
	return (y-x)

x0 = 0
y0 = 1

x = np.linspace(0,2,21)

# plt.figure()

deltax = 0.04
xvec = np.linspace(x0,x[-1],((x[-1]-x0)/deltax)+1)
yvecEU = []
yvecEU_mod = []
yvecEU.append(y0)
yvecEU_mod.append(yvecEU[0] + dydx(xvec[0],yvecEU[0])*deltax)

for i in range(len(xvec)-1):
	yvecEU.append(yvecEU[i] + dydx(xvec[i],yvecEU[i])*deltax)
	yvecEU_mod.append(yvecEU_mod[i] + (dydx(xvec[i],yvecEU_mod[i]) + dydx(xvec[i+1],yvecEU[i+1]))*deltax)
	plt.plot(xvec[i],yvecEU[i], '.')
print(i)
plt.show()

##################################