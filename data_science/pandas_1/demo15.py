#filter
import numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/soura/OneDrive/Documents/customer1.txt',sep=',',header=None)
df.columns=['Id','fname','lname','age','prof','location']
#for filter(to collect data based on condition) use loc() function
#newdf=olddfname.loc[olddf['columnname']condition]
#age>50
df1=df.loc[df['age']>50]
print(df1)
print('**'*100)

#loc=india
df2=df.loc[df['location']=='india']
print(df2)
print('**'*100)

#loc=us, print fname,lname,age,prof
df3=df.loc[df['location']=='us'] [['fname','lname','age','prof']]
print(df3)
print('**'*100)

#for more than 1 condition
# df1=df.loc[(df['column1']condition1)&(df['column2']condition2)]
#age>50 and loc=india
df4=df.loc[(df['age']>50)&(df['location']=='india')]
print(df4)
