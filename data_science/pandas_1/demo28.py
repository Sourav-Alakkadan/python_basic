import numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/soura/Downloads/customer5 (1).txt',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','loc','salary']
#1. Each profession count  [count desc]
df1=df.groupby('prof') ['prof'].count().sort_values(ascending=False)
print(df1)

#2. Each profession total salary  [salary desc]
df2=df.groupby('prof') ['salary'].sum().sort_values(ascending=False)
print(df2)

#3. Each country maximum salary
df3=df.groupby('loc') ['salary'].max()
print(df3)

#4. Each profession min salary
df4=df.groupby('loc') ['salary'].min()
print(df4)

#5. Each country average salary
df5=df.groupby('loc') ['salary'].mean()
print(df5)