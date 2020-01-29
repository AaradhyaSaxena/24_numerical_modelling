# ######## Heat1D_explicit
# import numpy as np
# import matplotlib.pyplot as plt

# L =100
# Tmagma =1200
# Trock =300
# kappa = 0.0000001
# W =5
# day = 3600*24
# dt = 1*day

# nx = 201
# nt = 100*24

# dx = L/(nx*(1.0)-1)
# x = np.linspace(-L/2, L/2,(nx-1))

# T = np.ones(len(x))*Trock
# T[abs(x)<=W/2] = Tmagma

# time =0
# for n in range(nt-1):
# 	Tnew = np.zeros(nx-1)
# 	for i in range(1,nx-2):
# 		Tnew[i] = T[i] + (kappa*dt/(dx*dx))*(T[i-1]-2*T[i]+T[i+1])

# 	Tnew[0] = T[0]
# 	Tnew[nx-2] = T[nx-2]

# 	T = Tnew
# 	time = time+dt

# 	# Ymat[n,:] = n*dt*np.ones(1,nx)
# 	# Xmat[n,:] = x
# 	# Tmat[n,:] = Tnew

# plt.figure()
# plt.plot(x,Tnew)
# plt.show()	

#########################################	
### Heat1D_implicit

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

L =100
Tmagma =1200
Trock =300
kappa = 0.0000001
W =5
day = 3600*24
dt = 1*day

nx = 201
nt = 100

dx = L/(nx*(1.0)-1)
x = np.linspace(-L/2, L/2,(nx-1))

T = np.ones(len(x))*Trock
T[abs(x)<=W/2] = Tmagma

A = np.zeros((nx-1,nx-1))
A[0,0] = 1
sx = kappa*dt/(dx)**2
for i in range(1,nx-2):
	A[i,i-1] =-sx
	A[i,i] = (1+2*sx)
	A[i,i+1] = -sx

A[nx-2,nx-2] = 1

nt=2400
time =0
for n in range(nt-1):
	Tnew = np.matmul(inv(A),T)
	Tnew[0] = T[0]
	Tnew[nx-2] = T[nx-2]

	T = Tnew
	time = time+dt

plt.figure()
plt.plot(x,Tnew)
plt.show()



