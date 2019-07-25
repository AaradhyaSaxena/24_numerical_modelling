import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,1000,100)

v0 = 500
theta = 60
g=9.8

# x = v0*t*np.cos(theta)
# y = v0*t*np.sin(theta) - 0.5*g*np.power(t,2)

# %matplotlib
# plt.plot(x,y)

###--------------
# ## Assignment1

# X = lambda v0,t,theta: v0*t*np.cos(theta)
# Y = lambda v0,t,theta: v0*t*np.sin(theta) - 0.5*g*np.power(t,2)

# # print(X(v0,t,theta))
# # print(Y(v0,t,theta))

# ##--------------------

# theta = [30,45,80]

# for i in range(len(theta)):
# 	print(i)
# 	plt.figure()
# 	plt.plot(X(v0,t,theta[i]),Y(v0,t,theta[i]))
# 	plt.show()

###---------------
## Assignment2

data = "data/XZ_GOAT_BHZ.dat"

file = open(data, 'rb')
f = np.loadtxt(file)

%matplotlib
plt.plot(f)

print(f)








