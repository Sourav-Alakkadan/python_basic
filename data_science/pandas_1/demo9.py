#how to add a new column into a data frame
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
#add new column
df['Gender']=['M','M','M','M','M','F','F']
print(df)
print('*'*100)

#delete a column
df1=df.drop(['prof','age'],axis=1)
print(df1)
print('*'*100)

#rename a column
#fname===>firstname
df2=df1.rename(columns={'fname':'first_name'})
print(df2)