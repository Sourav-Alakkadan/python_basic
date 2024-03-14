#1.age>50 fname,lname,age,prof
#2.work in india fname.lname,age,prof
#3.work in uk full data
#4.age>50 and loc india fname,age,loc
#5.work in dance fname,lname,age
#6.work in pilot fname,lname,age
#7.work in india and age range 25 to 40 fname,lanme,age
#8.each prof count
#9.each country count
#10.each age group count

f=open('C:/Users/soura/OneDrive/Documents/customer1.txt','r')
dic={}
#1.
# for i in f:
#     data=i.rstrip('\n').split(',')
#     age=data[3]
#     if age>'50':
#         print(data[1:5])

#2.
# for i in f:
#     data=i.rstrip('\n').split(',')
#     loc=data[-1]
#     if loc=='india':
#         print(data[1:5])

#3.
# for i in f:
#     data=i.rstrip('\n').split(',')
#     loc=data[-1]
#     if loc=='uk':
#         print(data[1:])

#4.
# for i in f:
#     data=i.rstrip('\n').split(',')
#     age=data[3]
#     loc=data[5]
#     if (age>'50')&(loc=='india'):
#         print(data[1:6:2])

#5.
# for i in f:
#     data=i.rstrip('\n').split(',')
#     prof=data[4]
#     if prof=='Dancer':
#         print(data[1:4])

#6.
# for i in f:
#     data = i.rstrip('\n').split(',')
#     prof=data[4]
#     if prof=='Pilot':
#         print(data[1:4])

#7.
# for i in f:
#     data = i.rstrip('\n').split(',')
#     loc=data[-1]
#     age=data[-3]
#     if ('25'<age<'40')&(loc=='india'):
#         print(data[1:4])

#8.
# for i in f:
#     data = i.rstrip('\n').split(',')
#     prof=data[-2]
#     if prof not in dic:
#         dic[prof]=1
#     else:
#         dic[prof]+=1
# for k,v in dic.items():
#     print(k,'','',v)

#9.
# for i in f:
#     data = i.rstrip('\n').split(',')
#     loc=data[-1]
#     if loc not in dic:
#         dic[loc]=1
#     else:
#         dic[loc]+=1
# for k,v in dic.items():
#     print(k,'','',v)

#10.
for i in f:
    data = i.rstrip('\n').split(',')
    age=data[3]
    if age not in dic:
        dic[age]=1
    else:
        dic[age]+=1
for k,v in dic.items():
    print(k,'','',v)
