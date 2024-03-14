#max()
#newdfname=olddfname.groupby('columnname') ['columnname'].max()
import numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/soura/OneDrive/Documents/customer1.txt',sep=',',header=None)
df.columns=['Id','fname','lname','age','prof','location']
#each prof max age
df1=df.groupby('prof') ['age'].max()
print(df1)