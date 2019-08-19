### lab_2
### interpolation

### quadratic interpolation

import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from numpy.linalg import inv

x = np.array([0,1,2,3,4])
y = np.array([0,2,3,5,7])

big_matrix = np.array([[0,0,1,0,0,0,0,0,0,0,0,0]
					 ,[1,1,1,0,0,0,0,0,0,0,0,0]
					 ,[0,0,0,1,1,1,0,0,0,0,0,0]
					 ,[0,0,0,4,2,1,0,0,0,0,0,0]
					 ,[0,0,0,0,0,0,4,2,1,0,0,0]
					 ,[0,0,0,0,0,0,9,3,1,0,0,0]
					 ,[0,0,0,0,0,0,0,0,0,9,3,1]
					 ,[0,0,0,0,0,0,0,0,0,16,4,1]
					 ,[2,1,0,-2,-1,0,0,0,0,0,0,0]
					 ,[0,0,0,4,1,0,-4,-1,0,0,0,0]
					 ,[0,0,0,0,0,0,6,1,0,-6,-1,0]
					 ,[1,0,0,0,0,0,0,0,0,0,0,0]])

y1 = np.array([0,2,2,3,3,5,5,7,7,0,0,0,0])

coeffe = np.matmul(inv(big_matrix), y1)

print(coeffe)



# f = interpolate.interp1d(x, y, kind='cubic')

# xnew = np.arange(0,4,0.01)
# ynew = f(xnew)

# plt.plot(x,y, "o",xnew, ynew,"-")
# plt.show()

