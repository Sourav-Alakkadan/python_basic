import numpy as np
import pandas as pd
df1=pd.read_csv("C:/Users/soura/Downloads/student",sep=',',header=None)
df1.columns=['name','roll.no']
print(df1)
print('**'*100)
df2=pd.read_csv("C:/Users/soura/Downloads/results",sep=',',header=None)
df2.columns=['roll.no','result']
print(df2)
print('**'*100)
df3=pd.merge(df1,df2,on='roll.no',how='inner').loc[df2['result']=='pass'] [['name','roll.no','result']]
print(df3)