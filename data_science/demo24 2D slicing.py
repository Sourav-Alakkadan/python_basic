#2D slicing
import numpy as np
a=np.array([[2,4,6,8,3],[1,3,4,6,8],[8,4,6,3,9],[0,4,1,3,9]])
#print(a[rows,columns])
print(a[1:,:3])      #r=1,2,3,4 & c=0,1,2
print(a[1:4,:3])     #r=1,2,3   & c=0,1,2,3
print(a[2:,2:4])     #r=2,3     & c=2,3
print(a[1:4:2,2::2]) #r=1,3     & c=2,4
##print zeroth row and column
print(a[0,])
print(a[:,0])