#2D 3*4 matrics(reshape)
import numpy as np
a=np.array([[2,4,6,8],[7,4,8,3],[9,1,5,3]])
print(a)

#to change the order of the matrics we use reshape function
#reshape()
b=a.reshape([4,3])
print(b)
#to change the order the no of elements should be same
#ie,(3*4)=12,(4,3)=12 we cannot change the order into (5*4)
#because its total=20