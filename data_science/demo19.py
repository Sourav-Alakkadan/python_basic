import numpy as np
a=np.array([[1,3,5,7],[5,2,6,8],[8,4,6,3]])
b=np.sum(a)
print(b)

#In 2D there are row and columns so we use axis to seperate rows and columns
#axis=0 ===> columns
#axis=1 ===> rows
c=np.sum(a,axis=0)
print(c)
d=np.sum(a,axis=1)
print(d)