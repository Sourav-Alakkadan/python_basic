#Dframe
#1st 10 row
#data type
#total missing value
#fill missing value
import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/soura/Downloads/missing_data1.csv",header=None)
#1.
df2=df.head(10)
print(df2)
print('**'*100)
#2.
print(df.dtypes)
print('**'*100)
#3.
print(df.isna().sum())
print('**'*100)
#4.
df3=df.fillna(2024/11/20)
print(df3.isna().sum())