#min()
#df1=df.groupby('colname') ['colname'].min()
import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/soura/Downloads/Temperature",sep=' ',header=None)
df.columns=['year','temp']
df1=df.groupby('year') ['temp'].min().sort_values()
print(df1)