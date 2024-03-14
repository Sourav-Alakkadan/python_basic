#create a list[10,15,5,12,8,12,14,4]
lst=[10,15,5,12,8,12,14,4]   #sum=80
lst1=[]
sum=0
for i in lst:
    sum=i+sum
for i in lst:
    lst1.append(sum-i)
print(lst1)
