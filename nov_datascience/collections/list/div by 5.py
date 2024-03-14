#print elements from 1 to 50 and div by 5
lst=[]
for i in range(1,51):
    if(i%5==0):
        lst.append(i)
print(lst)