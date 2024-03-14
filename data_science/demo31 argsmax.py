#argmax
#it is used to print the index of the highest value
#1D
import numpy as np
a=np.array([2,4,6,8,1,3,7,9,5])
print(a)
b=np.argmax(a)
print(b)
print('*'*100)

#2D
import numpy as np
a=np.array([[3,2,5,8],[7,4,9,2],[6,3,9,5],[0,3,9,5]])
print(a)
b=np.argmax(a)
print(b)
#row wise argmax
c=np.argmax(a,1)
print(c)
#column wise argmax
d=np.argmax(a,0)
print(d)