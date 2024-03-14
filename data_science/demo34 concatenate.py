#1D
#join two array
# import numpy as np
# a=np.array([2,4,8,3,9,1,0,6,7])
# b=np.array([9,3,4,1,0,8,5,7,2])
# c=np.concatenate((a,b))
# print(c)

#2D
import numpy as np
a=np.array([[3,2,5,8],[7,4,9,2],[6,3,9,5],[0,3,9,5]])
b=np.array([[6,3,2,8],[7,4,5,1],[0,5,8,3],[8,3,5,1]])
c=np.concatenate((a,b))   #column wise concatenation
print(c)

#row wise concatenation
d=np.concatenate((a,b),1)
print(d)