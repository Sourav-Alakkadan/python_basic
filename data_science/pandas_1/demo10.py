#how to change external file into data frame
import numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/soura/OneDrive/Documents/customer1.txt',sep=',',header=None)
# print(df)

#give column name
df.columns=['Id','fname','lname','age','prof','location']
print(df)
print('**'*100)

#print first 10 row
print(df.head(10))
print('**'*100)

#print last 10 rows
print(df.tail(10))
print('**'*100)

#to print in b/w rows we use iloc() function
df1=df.iloc[3:11]
print(df1)
print('**'*100)

df2=df.iloc[::10] #0 to last with iteration 10
print(df2)