#Dictionary

#1.define
dic={}
print(dic)

#dictionary is a key-value pair

# id:101
# fname=anu
# lname=k
# age=27
# prof=python

#1.how to define
dic={'id':101,'fname':'Vinay','lname':'k','age':28,'prof':'bigdata'}

#2.support hetrogenous values
dic1={'id':101,'fname':'Vinay','lname':'k','age':28,'prof':'bigdata'}
print(dic1)

#3 insertion is preserved

#4.Not support duplicate key but support duplicate values
dic2={'id':101,'fname':'Vinay','lname':'k','age':26,'age':28,'mark':70}
print(dic2)

dic3={'id':101,'fname':'Vinay','lname':'k','age':28,'mark':28}
print(dic3)