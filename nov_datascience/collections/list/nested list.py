#nested list
lst=[[101,'vinay','k',29,'bigdata',1000],
     [102,'amal','h',30,'python',1500],
     [103,'vivek','m',28,'testing',2000],
     [104,'arjun','a',31,'testing',3000],
     [105,'vineeth','o',32,'bigdata',3500]]
# for i in lst:
#     print(i)
#if we use for loop in nested list one by one list is printed

#print only if age is above 30 data
# for i in lst:
#     if(i[3]>30):
#         print(i)

#print 1stname,lastname,age,prof if age less than 30
# for i in lst:
#     if(i[3]<30):
#         print(i[1:5])


#1.print 1stname,lastname,age if age=30
for i in lst:
    if(i[3]==30):
        print(i[1:4])

#2.print fname,lname,age,prof if prof is bigdata
for i in lst:
    if(i[4]=='bigdata'):
        print(i[1:5])

#3.print fname,age,salary if prof is python
for i in lst:
    if(i[4]=='python'):
        print(i[1::2])    # 1 to 6 with itereting 2 ie,(1,3,5)

#4.print fname,age,salary if prof is bigdata and age above 27
for i in lst:
    if(i[4]=='bigdata')&(i[3]>27):
        print(i[1:6:2])    # 1 to 6 with itereting 2 ie,(1,3,5)

#5.total salary of all employ
salary=0
for i in lst:
    salary=salary+i[5]
print(salary)



