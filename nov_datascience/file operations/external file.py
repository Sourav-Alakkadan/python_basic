#read from external file

f=open('C:/Users/soura/OneDrive/Documents/sample4.txt','r')
#1.age above 22 fname,lname,age
# for i in f:
#     # print(i)
#     data=i.rstrip('\n').split(',')
#     age=data[3]
#     if age>'22':
#         print(data[1:4])

#2.age=24,fname,lname,age,ph
# for i in f:
#     data=i.rstrip('\n').split(',')
#     age=data[3]
#     if age=='24':
#         print(data[1:5])

#3.chennai location fname,age,location
# for i in f:
#     data=i.rstrip('\n').split(',')
#     location=data[5]
#     if location=='Chennai':
#         print(data[1:6:2])

#4.age>23 and loc chennai fname,lname,age,ph,loc
# for i in f:
#     data=i.rstrip('\n').split(',')
#     age=data[3]
#     loc=data[5]
#     if (age>'23') & (loc=='Chennai'):
#         print(data[1:6])

#5.each location count
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    loc=data[-1]
    if loc not in dic:
        dic[loc]=1
    else:
        dic[loc]+=1
for k,v in dic.items():
    print(k,'','',v)
