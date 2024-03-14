 #Binarg search algorithm

#lst=[1,4,2,5,7,3,9,8]
#1. sort the given list in ascending order
#lst=[1,2,3,4,5,7,8,9]

#2.lower and upper
#lower=0
#upper=len(lst)-1  ie,9-1=8

#3.calculate the mid =(lower+upper)//2  ie,8//2=4
#condition
#a) search>lst[mid]   ie,lst[4]=5  (8>5)
          #lower=mid+1
#b) search<lst[mid]   (2<5)
          #upper=mid-1
#c) search==lst[mid]
          #element found

#problem:
lst=[5,32,11,20,55,9,43,18,15,3,6]
num=int(input('Enter a number:'))
flag=0
lst.sort()
lower=0
upper=len(lst)-1
for i in range(lower,upper):
    mid=(lower+upper)//2
    if(num>lst[mid]):
        lower=mid+1
    elif(num<lst[mid]):
        upper=mid-1
    elif(num==lst[mid]):
        flag=1
        break
if(flag==1):
    print('Number is present')
else:
    print('Number is not present')