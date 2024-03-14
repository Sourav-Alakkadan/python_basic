lst1=[]
for i in range(1,31):
    lst1.append(i)
print(lst1)
f=list(filter(lambda i:i%2==1,lst1))
print(f)
f2=list(map(lambda x:x**2,f))
print(f2)