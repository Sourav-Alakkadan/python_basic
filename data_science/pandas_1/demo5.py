#nested list
import numpy as np
import pandas as pd
lst=[[100,'vinay','k',27,'bigdata',10000,'kannur'],
     [101,'sourav','a',22,'data science',12000,'payyanur'],
     [102,'jithin','tp',25,'python',15000,'kasargod'],
     [104,'abhijith','m',21,'mean',10000,'ernakulam'],
     [105,'arjun','s',23,'testing',20000,'kollam'],
     [106,'arya','t',22,'data science',15000,'kannur'],
     [107,'amala','p',26,'asp.net',12000,'calicut']]
#data frame
df=pd.DataFrame(lst,columns=['id','fname','lname','age','prof','salary','location'])
print(df)
print('**'*100)

print(df.shape)
print('**'*100)

print(df.head(2))
print('**'*100)

print(df.tail(3))