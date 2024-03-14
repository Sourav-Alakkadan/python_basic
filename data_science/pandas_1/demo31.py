#id equal
#1.name,age,loc,date,amt
#2.name.loc,salary,date,amt salary>2000
#3.age max employee name,age,salary,date
#4.latest date name,age,loc,date,amt
#5.salary>2000 and amt>1000 name,age,salary,amt
import numpy as np
import pandas as pd
df1=pd.read_csv("C:/Users/soura/Downloads/custom.txt",sep=',',header=None)
df1.columns=['cus.id','fname','age','loc','salary']
print(df1)
df2=pd.read_csv("C:/Users/soura/Downloads/order.txt",sep=',',header=None)
df2.columns=['or.id','pur.date','cus.id','amt']
print(df2)
print('**'*100)
#1.
df3=pd.merge(df1,df2,on='cus.id',how='inner') [['fname','age','pur.date','amt']]
print(df3)
print('**'*100)
#2.
df4=pd.merge(df1,df2,on='cus.id',how='inner').loc[df1['salary']>2000] [['fname','loc','salary','amt']]
print(df4)
print('**'*100)
#3.
df5=pd.merge(df1,df2,on='cus.id',how='inner').sort_values(by='age') [['fname','age','salary','pur.date']].tail(1)
print(df5)
print('**'*100)
#4.
df6=pd.merge(df1,df2,on='cus.id',how='inner').sort_values(by='pur.date') [['fname','age','loc','pur.date','amt']].tail(1)
print(df6)
print('**'*100)
#5.
df7=pd.merge(df1,df2,on='cus.id',how='inner').loc[(df1['salary']>2000)&(df2['amt']>1000)] [['fname','age','salary','amt']]
print(df7)