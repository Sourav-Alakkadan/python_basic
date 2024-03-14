#how to handle missing value

import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/soura/Downloads/missing_data1.csv")
print(df)
print(df.isna().sum())
#df.fillna(200,inplace=True)
print(df)
print('**'*100)

#replace missing value in specific column
# df['Calories'].fillna(275,inplace=True)
# df['Date'].fillna("'2024/01/30'",inplace=True)
# print(df)
# print('**'*100)

#replace missing value logically
# x=df['Calories'].mean()
# df['Calories'].fillna(x,inplace=True)
# print(df)

# or
# y=df['Calories'].median()
# df['Calories'].fillna(y,inplace=True)
# print(df)
# or

# z=df['Calories'].mode()[0]
# df['Calories'].fillna(z,inplace=True)
# k=df['Date'].mode()[0]
# df['Date'].fillna(k,inplace=True)
# print(df)

#drop function
#it is used to drop or delete all the row containing missing values
#df.dropna(inplace=True,ignore_index=True) #it will delete the containing missing values ie, 18,22,28
#to correct the index no use ignore_index function
#print(df)

df.dropna(subset=['Date'],inplace=True)
print(df)
#it will delete missing value in date row only