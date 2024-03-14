#2D dot product
import numpy as np
a=np.array([[3,5,7],[8,5,1],[9,2,7]])
b=np.array([[6,4,8],[3,4,7],[2,4,9]])
#in 2D dot product will calculated by elements of 1st row * elements of 1st columns
c=np.dot(a,b)
print(c)
#order need not be same but first matrics no.of columns should be same as 2nd matrics no.of rows
#(3*4) & (4*5) possible
#(3*5) & (3*4) not possible
