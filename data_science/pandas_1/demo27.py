#Mean()
#to calculate the average of each column
import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/soura/Downloads/Temperature",sep=' ',header=None)
df.columns=['year','temp']
df1=df.groupby('year') ['temp'].mean().sort_values()
print(df1)