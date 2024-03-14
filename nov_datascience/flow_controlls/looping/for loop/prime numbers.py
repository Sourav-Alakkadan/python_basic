#check given number is prime or not

num=int(input('Enter a number:'))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag=1
if(flag==0):
        print("Number is prime")
else:
        print('Number is not prime')