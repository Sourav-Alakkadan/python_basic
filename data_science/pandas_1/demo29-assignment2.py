#orderid,purchasedate,customerid,payamt,categorise,product,city,state,paymethod
import  numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/soura/Downloads/txn.txt",sep=',',header=None)
df.columns=['oid','pudate','cusid','payamt','cate','prdt','city','state','paymtd']
print(df)
print('*1'*1)
#1.Find Row count
print(df.shape)
print('*2'*1)
#2.jan month oid,cusno,category,product,state row count
df1=df.loc[(df['pudate']>='01-01-2011')&(df['pudate']<='01-31-2011')] [['oid','cusid','cate','prdt','state']]
print(df1)
print(df1.shape)
print('*3'*1)
#3.July Month oid,cusno,category,product,state row count
df2=df.loc[(df['pudate']>='07-01-2011')&(df['pudate']<='07-31-2011')]  [['oid','cusid','cate','prdt','state']]
print(df2)
print(df2.shape)
print('*4'*1)
#4.Each category [count desc sort]
df3=df.groupby('cate') ['cate'].count().sort_values(ascending=False)
print(df3)
print('*5'*1)
#5.Category full deatils
df4=df.loc[df['cate']=='Outdoor Recreation']
print(df4)
print('*6'*1)
#6.Each paymethod count
df5=df.groupby('paymtd') ['paymtd'].count()
print(df5)
print('*7'*1)
#7.jan-july month purchase count [include]
df6=df.loc[(df['pudate']>='01-01-2011')&(df['pudate']<='07-31-2011')]
print(df6.shape)
print('*8'*1)
#8.Each category total amount
df7=df.groupby('cate') ['payamt'].sum()
print(df7)
print('*9'*1)
#9.Each category maximum amount
df8=df.groupby('cate') ['payamt'].max()
print(df8)
print('*10'*1)
#10.Each category avg amount
df9=df.groupby('cate') ['payamt'].mean()
print(df9)
print('*11'*1)
#11.total amount by cash and credit card
df10=df.groupby('paymtd') ['payamt'].sum()
print(df10)
print('*12'*1)
#12.Indoor games ,total amount
df11=df.loc[df['cate']=='Indoor Games'].groupby('paymtd') ['payamt'].sum()
print(df11)
print('*13'*1)
#13. Each state count
df12=df.groupby('state') ['state'].count().sort_values()
print(df12)