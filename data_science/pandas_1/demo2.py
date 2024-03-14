#Dictionary into series
import numpy as np
import pandas as pd
dic={'name':'vinay','id':101,'age':27,'prof':'data science'}
a=pd.Series(dic)
print(a)
#when we change dic into series there no index value , the key act as index value in this case
b=pd.Series(dic,['id','name','prof'])
print(b)