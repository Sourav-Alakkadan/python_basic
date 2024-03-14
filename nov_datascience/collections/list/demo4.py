lst=[1,2,3,4,5,6,7,8,9]
oddsum=0
for i in lst:
    if(i%2==1):
        oddsum=i+oddsum
print(oddsum)