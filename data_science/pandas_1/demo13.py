#how handle missing value (introduction)
import numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/soura/OneDrive/Documents/customer1.txt',sep=',',header=None)
df.columns=['Id','fname','lname','age','prof','location']
print(df.isna().sum())

#to fill the missing value use fillna() function
df2=df.fillna('India')
print(df2.isna().sum())