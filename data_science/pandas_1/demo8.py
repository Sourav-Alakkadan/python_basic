#dictionary
import numpy as np
import pandas as pd
dic={'id':[1,2,3,4,5],'fname':['amal','akhil','karthik','sooraj','alok'],
     'lname':['k','k','m','sm','p'],'age':[21,18,22,20,19],
     'course':['bigdata','python','mearn','testing','data science'],
     'loc':['kannur','calicut','kasargod','kollam','kochi']}
df=pd.DataFrame(dic)
print(df.describe())
print('*'*100)

print(df.describe(include='O'))
print('*'*100)

print(df.describe(include='all'))