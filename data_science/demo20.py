#2D matrics operation
import numpy as np
a=np.array([[1,4,3],[2,5,8],[6,9,4]])
b=np.array([[6,3,8],[9,2,3],[2,6,4]])
#to add two matrics we use add() function
#to perfrom this both matrics should have same order
c=np.add(a,b)
print(c)
#to subtract we use subtract() function
d=np.subtract(a,b)
print(d)
#to multiply we use multiply() function
e=np.multiply(a,b)
print(e)
#to divide we use divide() function
f=np.divide(a,b)
print(f)
#to find the square of a matrics we use square() function
g=np.square(a)
print(g)
#to find the square root we use the sqrt() function
h=np.sqrt(a)
print(h)
