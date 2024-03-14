#Joining
#4 types of joining:
#1.inner joining
#2.left outer joining
#3.right outer joining
#4.full outer joining
import numpy as np
import pandas as pd
dic1={'id':[101,102,103,104,105],'fname':['vinay','alex','amal','akhil','ajay'],
      'lname':['m','p','k','a','vv'],'age':[23,22,25,21,24]}
dic2={'id':[104,105,106,107,108],'prof':['mearn','python','data science','testing','asp.net'],
      'loc':['kannur','calicut','kochi','kollam','wayanad'],'salary':[15000,10000,13000,12000,9000]}
df1=pd.DataFrame(dic1)
df2=pd.DataFrame(dic2)
print(df1)
print(df2)
print('**'*100)
#Inner joining
#to join 2 data frame there should be any common data or filled (ie,column name)
#if we join df1 & df2 the id is common in that 104&105 are common so its full data will be printed
#syntax:
#newdfname=pd.merge(df1,df2,on='commoncolname',how='inner')
df3=pd.merge(df1,df2,on='id',how='inner')
print(df3)
print('**'*100)
#it will full data

#fname,lname,age,salary above 13000
df4=pd.merge(df1,df2,on='id',how='inner').loc[df2['salary']>13000] [['fname','lname','age','salary']]
print(df4)
print('**'*100)

#id equal age max 1 empolyee fname,lname,prof,salary
df5=pd.merge(df1,df2,on='id',how='inner').sort_values(by='age') [['fname','lname','prof','salary']].tail(1)
print(df5)
print('**'*100)