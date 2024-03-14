#2D 5*4
#1.4*5
#2.2*10
#3.1 dimensional
#4.3D===>(4,5)
import numpy as np
a=np.array([[1,2,3,4],[6,7,8,9],[2,4,6,8],[1,3,5,7],[4,3,7,9]])
b=a.reshape([4,5])
print(b)
c=a.reshape([2,10])
print(c)
d=a.reshape([20])
print(d)
e=a.reshape([1,4,5])
print(e)