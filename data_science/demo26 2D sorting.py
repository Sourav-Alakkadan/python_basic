#sorting in 2D
# [[3 2 5 8]
#  [7 4 9 2]
#  [6 3 9 5]
#  [0 3 9 5]]
import numpy as np
a=np.array([[3,2,5,8],[7,4,9,2],[6,3,9,5],[0,3,9,5]])
#row wise sorting ascending order
b=np.sort(a)
print(b)
print('*'*1000)

#column wise sorting ascending order
c=np.sort(a,0)
print(c)
print('*'*1000)

#row wise sorting descending
d=np.sort(a,1)[:,::-1]
print(d)
print('*'*1000)

#column wise sorting descending
e=np.sort(a,0)[::-1,:]
print(e)