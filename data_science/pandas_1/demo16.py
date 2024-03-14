#[id,fname,lname,age,phno,location]
#1.age=22 fname,lname,age,phno
#2.chennai work fname,lname,age,phno
#3.chennai work and age>23 fname,lname,age,phno
import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/soura/Downloads/sample4.txt",header=None)
df.columns=['Id','fname','lname','age','ph.no','location']
print(df)
print('**'*100)
#1.
df1=df.loc[df['age']==22] [['fname','lname','age','ph.no']]
print(df1)
print('**'*100)
#2.
df2=df.loc[df['location']=='Chennai'] [['fname','lname','age','ph.no']]
print(df2)
print('**'*100)
#3.
df3=df.loc[(df['location']=='Chennai')&(df['age']>23)] [['fname','lname','age','ph.no']]
print(df3)