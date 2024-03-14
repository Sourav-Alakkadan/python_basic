#age max print fname,lname,age
lst=[[101,'vinay','k',29,'bigdata',1000],
     [102,'amal','h',30,'python',1500],
     [103,'vivek','m',38,'testing',2000],
     [104,'arjun','a',31,'testing',3000],
     [105,'vineeth','o',32,'bigdata',3500]]
oldest=0
flag=0
for i in lst:
    if(i[3]>oldest):
        oldest = i[3]
        flag=i
print(flag[1:4])
