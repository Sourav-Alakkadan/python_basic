#List into series
import numpy as np
import pandas as pd
lst=[2,4,10,5,1,8,6,9,0,3,7]
s=pd.Series(lst)
print(s)

#to print the data type use dtype function
print(s.dtype)
#head():it print 1st 5 values(5 is defualt), if enter 7 it will print 7 values
print(s.head())
print(s.head(7))
#tail():it print the last values
print(s.tail())
print(s.tail(2))
#shape():total no.of elements,in 2D order
print(s.shape)