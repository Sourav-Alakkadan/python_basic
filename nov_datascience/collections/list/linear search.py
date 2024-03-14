#linear search algorithm
lst=[1,5,10,15,12,13,14,17,20,25,30,35,40,45,60]
num=int(input('Enter a number:'))
flag=0
for i in lst:
    if(i==num):
        flag=1
if(flag==1):
    print('Number present')
else:
    print('Number not present')

#linear search alogrithm
#drawbacks
#time comlexity