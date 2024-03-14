import numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/soura/OneDrive/Documents/customer1.txt',sep=',',header=None)
df.columns=['Id','fname','lname','age','prof','location']
x=df.iloc[0:,:-1]
print(x)
y=df.iloc[:,-1]
print(y)
print('**'*100)

#how to collect columns
df1=df[['fname','age','location']]
print(df1)

#1st 50 employee fname,lname,age,prof
df2=df[['fname','lname','age','prof']].head(50)
print(df2)