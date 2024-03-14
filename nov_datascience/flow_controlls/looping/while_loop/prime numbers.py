num=int(input('Enter a number:'))
i=2
flag=0
while(i<=num):
    if(num%i==0):
        flag=1
        break
    i+=1
if(flag==0):
    print('number is prime',num)
else:
    print('number is not prime',num)