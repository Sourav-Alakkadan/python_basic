#2D argsort

import numpy as np
a=np.array([[3,2,5,8],[7,4,9,2],[6,3,9,5],[0,3,9,5]])
print(a)
print('*'*100)

#row wise argsort
b=np.argsort(a)
print(b)
print('*'*100)

#column wise argsort
c=np.argsort(a,0)
print(c)

