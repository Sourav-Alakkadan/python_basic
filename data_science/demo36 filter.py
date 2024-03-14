#filter
#it is used to print elements that satisfies certain condition
#in this method there is no function used

#1D
import numpy  as np
a=np.array([40,41,42,43,44,45,46,47,48,49])
b=(a>45)
c=a[b]
print(c)

#even numbers
d=(a%2==0)
e=a[d]
print(e)
