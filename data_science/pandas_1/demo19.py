#customer
import numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/soura/OneDrive/Documents/customer1.txt',sep=',',header=None)
df.columns=['Id','fname','lname','age','prof','location']
print(df)
#1.age max 10 employee fname,lname,age,prof,loc
df1=df.sort_values(by='age') [['fname','lname','age','prof','location']].tail(10)
print(df1)
print('**'*100)

#2.age min 5 employee fname,lname,age,prof,loc
df2=df.sort_values(by='age') [['fname','lname','age','prof','location']].head(5)
print(df2)
print('**'*100)

#3.india work,age max 3 employee fname,lname,age,prof
df3=df.loc[df['location']=='india'].sort_values(by='age') [['fname','lname','age','prof']].tail(3)
print(df3)
print('**'*100)

#4.doctor prof work
df4=df.loc[df['prof']=='Doctor'] [['fname','lname','age']]
print(df4)
print('**'*100)

#5. india work and prof doctor fname,lname,age
df5=df.loc[(df['location']=='india')&(df['prof']=='Doctor')] [['fname','lname','age']]
print(df5)
print('**'*100)

#6.uk and age range 40 to 70 fname,lname,age
df6=df.loc[(df['location']=='uk')&(df['age']>=40)&(df['age']<=70)] [['fname','lname','age']]
print(df6)
print('**'*100)

#7.Pilot prof work, age mxm 2 employee fname,lname,age
df7=df.loc[df['prof']=='Pilot'].sort_values(by='age') [['fname','lname','age']].tail(2)
print(df7)
print('**'*100)

#8.us, age minimum 3 employee fname,lname,age,prof
df8=df.loc[df['location']=='us'].sort_values(by='age') [['fname','lname','age']].head(3)
print(df8)
print('**'*100)

#9.Doctor prof age mxm 1 employee full data
df9=df.loc[df['prof']=='Doctor'].sort_values(by='age') \
       [['Id','fname','lname','age','prof','location']].tail(1)
print(df9)
print('**'*100)

#10.india and prof Doctor age minimum 1 employee full data
df10=df.loc[(df['location']=='india')&(df['prof']=='Doctor')]\
        .sort_values(by='age') [['Id','fname','lname','age','prof','location']].head(1)
print(df10)