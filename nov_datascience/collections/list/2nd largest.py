#find 2nd largest
lst=[1,6,8,15,20,3,100,75,40,45]
x=max(lst)
lst.remove(x)
second_largest=max(lst)
print('second largest:',second_largest)
