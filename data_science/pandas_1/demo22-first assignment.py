#Assignment
import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/soura/Downloads/movies_cleaned_pandas.csv",header=None)
df.columns=['Id','Movie name','Rel date','Rating','Duration']
print(df)
print('**'*100)
#1.row count
df1=df.count(axis=0)
print(df1.shape)
print('**'*100)
#2.
df2=df.drop_duplicates()
print(df2.shape)
print('**'*100)
#3.
df3=df.sort_values(by='Rel date',ascending=False)
print(df3)
print('**'*100)
#4.
df4=df.sort_values(by='Rating') [['Movie name','Rel date','Rating']].tail(5)
print(df4)
print('**'*100)
#5.
df5=df.sort_values(by='Rating') [['Movie name','Rel date','Rating']].head(3)
print(df5)
print('**'*100)
#6.
df6=df.groupby('Rel date')['Rel date'].count().sort_values(ascending=False)
print(df6)
print('**'*100)
#7.
df7=df.groupby('Rating') ['Rating'].count().sort_values(ascending=False)
print(df7)
print('**'*100)
#8.
df8=df.loc[(df['Rel date']==2008)&(df['Rating']>3)] [['Movie name','Rel date','Rating']]
print(df8.shape)
print('**'*100)
#9.
df9=df.sort_values(by='Duration') [['Movie name','Rel date','Rating','Duration']].tail(1)
print(df9)
print('**'*100)
#10.
df10=df.sort_values(by='Rating') [['Movie name','Rel date','Rating','Duration']].head(1)
print(df10)
print('**'*100)
#11.a)
df11=df.loc[(df['Rating']>4)&(df['Rel date']>2005)].sort_values(by='Rating').tail(1)
print(df11)
print('**'*100)
#11.b)
df12=df.loc[(df['Rating']>4)&(df['Rel date']>2005)].sort_values(by='Rating').head(1)
print(df12)
print('**'*100)
#12.
df13=df.loc[df['Rel date']==2008]
print(df13.shape)
print('**'*100)
#13.
df14=df.loc[(df['Rel date']>=1975)&(df['Rel date']<=2000)]
print(df14.shape)
print('**'*100)
#14.
df15=df.loc[(df['Rel date']>=1975)&(df['Rel date']<=2000)&(df['Rating']>3.5)]
print(df15.shape)