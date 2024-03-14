#1.age max 1 employee fname,lname,age,phno
#2.age min 2 employee fname,lname,age
#3.chennai work,age max 1 employee fname,lname,age

#order:
#loc
#sort
#column
#head/tail
import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/soura/Downloads/sample4.txt",header=None)
df.columns=['Id','fname','lname','age','ph.no','location']
print(df)
print('**'*100)
#1.
df1=df.sort_values(by='age') [['fname','lname','age','ph.no']].tail(1)
print(df1)
print('**'*100)
#2.
df2=df.sort_values(by='age',ascending=False) [['fname','lname','age','ph.no']].tail(2)
print(df2)
print('**'*100)
#3.
df3=df.loc[df['location']=='Chennai'].sort_values(by='age') \
       [['fname','lname','age','ph.no']] \
       .tail(1)
print(df3)