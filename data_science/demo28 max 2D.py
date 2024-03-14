#max & min in 2D
import numpy as np
a=np.array([[3,2,5,8],[7,4,9,2],[6,3,7,5],[0,3,11,5]])
print(a)
b=np.max(a)
print(b)
k=np.min(a)
print(k)

#row wise maximum & minimum
c=np.max(a,1)
print(c)
l=np.min(a,1)
print(l)

#column wise maximum & minimum
d=np.max(a,0)
print(d)
m=np.min(a,0)
print(m)