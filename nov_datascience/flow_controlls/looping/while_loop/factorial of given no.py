#find the factorial of the given number

#5  1*2*3*4*5
num=int(input('Enter a number:'))
factorial=1
i=1
while(i<=num):
    factorial=factorial*i
    i+=1
print(factorial)