import numpy as np
from numpy import linalg as LA
# We are using the linear algebra library
input = np.array([[2,-1] , [4,3]])
w,v = LA.eig(input)
print(w)
print(v)