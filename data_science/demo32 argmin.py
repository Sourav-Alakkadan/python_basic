#argmin()
#1D
import numpy as np
a=np.array([2,4,6,8,1,3,7,9,5])
print(a)
b=np.argmin(a)
print(b)

#2D
import numpy as np
a=np.array([[3,2,5,8],[7,4,9,2],[6,3,9,5],[0,3,9,5]])
print(a)
b=np.argmin(a)
print(b)
#row wise argmin
c=np.argmin(a,1)
print(c)
#column wise argmin
d=np.argmin(a,0)
print(d)