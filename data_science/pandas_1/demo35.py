#how to handle wrong format data
#if the data entered is in wrong format
#ie,in a data set of missing values in duration column 7 the duration is 450
#it is a wrong formate data
import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/soura/Downloads/missing_data1.csv")
print(df)
# df.loc[7,'Duration']=50
# print(df)

#if there is wrong formate in many places we use for loop
x=df['Calories'].mean()
for i in df.index:
    if(df.loc[i,'Calories']>400):
        df.loc[i,'Calories']=x
print(df)