#left outer joining
#df1   df2
#left  right

#it returns all row values from left data frame,plus matched values from
#right data frame or null in case of no matching values
#syntax:df3=pd.merge(df1,df2,on='commoncolname',how='left')
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
df3=pd.merge(df1,df2,on='id',how='left')
print(df3)
print('**'*100)

#3.right outer joining
#it return all row from right data frame, plus matched values from
#left data frame or null in case of no matching values
#syntax:df3=pd.merge(df1,df2,on='commoncolname',how='right')
df4=pd.merge(df1,df2,on='id',how='right')
print(df4)
print('**'*100)

#4.full outer joining
#it will be combining of left outer+right outer joining
#ie, left+right=full
#syntax:
df5=pd.merge(df1,df2,on='id',how='outer')
print(df5)