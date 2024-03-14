#sum()
#to calculate sum of each column
#ie,to calculate the total temp in each year
import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/soura/Downloads/Temperature",sep=' ',header=None)
df.columns=['year','temp']
df1=df.groupby('year') ['temp'].sum().sort_values()
print(df1)