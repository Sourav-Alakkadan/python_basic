#import movie file into data frame

import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/soura/Downloads/movies_cleaned_pandas.csv",header=None)
#it is a csv file so it is comma seperated
df.columns=['Id','Movie name','Release date','Rating','Duration']
print(df)