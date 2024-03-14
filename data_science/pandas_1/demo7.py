#describe function
import numpy as np
import pandas as pd
lst=[[100,'vinay','k',27,'bigdata',10000,'kannur'],
     [101,'sourav','a',22,'data science',12000,'payyanur'],
     [102,'jithin','tp',25,'python',15000,'kasargod'],
     [104,'abhijith','m',21,'mean',10000,'ernakulam'],
     [105,'arjun','s',23,'testing',20000,'kollam'],
     [106,'arya','t',22,'data science',15000,'kannur'],
     [107,'amala','p',26,'asp.net',12000,'calicut']]
df=pd.DataFrame(lst,columns=['id','fname','lname','age','prof','salary','location'])
print(df.describe())
#it will print numerical values
print('*'*100)

print(df.describe(include='O'))
#it will print other values
print('*'*100)

print(df.describe(include='all'))
#it will print all data
#NaN means there is no value ie, value cannot be taken in string