lst=[2,3,45,43,3,34,43,5,6,7,6,8]
lst1=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(len(lst1))
#merging