#Evaluating functions
#1.count()
#2.max()
#3.min()
#4.sum()
#5.mean()-average

#1.count()
#each columns count is calculated respectively
#ie,in customer
#groupby()===>1st step of evaluation function
#newdfname=olddfname.groupby('columnname') ['columnname'].count()

import numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/soura/OneDrive/Documents/customer1.txt',sep=',',header=None)
df.columns=['Id','fname','lname','age','prof','location']
#prof count
df1=df.groupby('prof') ['prof'].count().sort_values()
print(df1)
print('**'*100)

#location count
df2=df.groupby('location') ['location'].count().sort_values(ascending=False)
print(df2)
print('**'*100)

#work in india prof count
df3=df.loc[df['location']=='india'].groupby('prof') ['prof']\
      .count().sort_values()
print(df3)
