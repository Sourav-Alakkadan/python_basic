import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/soura/Downloads/Temperature",sep=' ',header=None)
df.columns=['year','temp']
#each year max year
df1=df.groupby('year') ['temp'].max().sort_values()
print(df1)