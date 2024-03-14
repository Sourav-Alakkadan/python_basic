#combine 2 series
import numpy as np
import pandas as pd
s1=pd.Series([7,3,4,1,9,5])
s2=pd.Series([10,2,3,8,9,4])
#append():to combine to 2 series use append function,here only values are combined
#to combine the index values we use ignore_index=True function
s3=s1._append(s2,ignore_index=True)
print(s3)
#add():
s4=s1.add(s2)
print(s4)
#subtract():
s5=s1.subtract(s2)
print(s5)
#multiply():
s6=s1.multiply(s2)
print(s6)
#divide():
s7=s1.divide(s2)
print(s7)
#NaN:not a number
#if the values are missing it will print NaN
#ie,if the index of 2 series are not same