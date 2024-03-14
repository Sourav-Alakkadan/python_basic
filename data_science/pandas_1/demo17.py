#sort function
#asc or desc ===>sort_values()
#df1=olddfname.sort_values(by='columnname')

import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/soura/Downloads/sample4.txt",header=None)
df.columns=['Id','fname','lname','age','ph.no','location']
print(df)
print('**'*100)
#sort according to age
df1=df.sort_values(by='age')
print(df1)
print('**'*100)
#it will sort in ascending order

df2=df.sort_values(by='age',ascending=False)
print(df2)
#it will sort in descending order