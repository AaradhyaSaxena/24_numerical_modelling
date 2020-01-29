######## LAB_4

import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from numpy.linalg import inv

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([2,4,5,8,7,8,5,9,12,16])

plt.scatter(x,y)
plt.show()

a, b = np.polyfit(x,y,1)

x = np.array([0,])
y = a*x + b

_ = plt.plot(x,y)
plt.show()

################################
########### matrix_inversion

from numpy.linalg import inv

x = np.array([[1,2,3,4,5,6,7,8,9,10],[1,1,1,1,1,1,1,1,1,1]])
y = np.array([2,4,5,8,7,8,5,9,12,16])

xtx = np.matmul(x,x.T)
xtx_inv = inv(xtx)

m = np.matmul(x,y)

inverted_matrix = np.matmul(xtx_inv, m)

a = inverted_matrix[0]
b = inverted_matrix[1]

x = np.array([0,10])
y = a*x + b

_ = plt.plot(x,y)
plt.show()

#################################
### grid search

x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,5,8,7,8,5,9,12,16]

m1 = np.linspace(0,2,100)
c1 = np.linspace(0,2,100)

y_calc =[]
error_l2 = []
error_l1 = []

# y_calc = m1[i]*x + c1
min_l1 = 100
min_l2 = 100

for i in m1:
	for j in c1:
		# print(i,j)
		# y_calc.append(i*x + j)
		# error_l2.append( (np.sum(np.square((i*x + j) - y)))/10 )
		# error_l1.append( (np.abs((i*x + j) - y))/10 )

		temp_l1 = (np.sum(np.square((i*x + j) - y)))/10
		temp_l2 = (np.abs((i*x + j) - y))/10

		if(temp_l1<min_l1):
			min_l1 = temp_l1
			m11 = i
			c11 = j

		if(temp_l2<min_l2):
			min_l2 = temp_l2
			m12 = i
			c12 = j

print(m11,m12,c11,c12)


min_error_l1 = np.min(error_l1)
min_error_l2 = np.min(error_l2)

##################################
#### probability distribution

k1 = np.sum(np.exp(-error_l1/np.std(error_l1)))
prob_l1 = np.exp(-error_l1/k1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(m11, c11, prob_l1)
plt.show()


k2 = np.sum(np.exp(-error_l2/np.std(error_l2)))
prob_l2 = np.exp(-error_l1/k2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(m12, c12, prob_l2)
plt.show()



