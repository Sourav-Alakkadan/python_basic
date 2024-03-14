#Zero matrics
#if all the numbers are zero
#eg:[0,0,0]

#how to 1D zero matrics
import numpy as np
# a=np.zeros([5],dtype=int)
# print(a)
#it will print in float data type ,to print it in int we use dtype=int inside matrics

#2D zero matrics
# a=np.zeros([3,4],dtype=int)
# print(a)

#3D zero matrics
a=np.zeros([2,3,3],dtype=int)
print(a)
print(a.ndim)
print(a.dtype)
print(a.size)