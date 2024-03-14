#take lower and upper limit from console and print prime numbers
lower=int(input('Enter lower limit:'))
upper=int(input('Enter upper limit:'))
for number in range(lower,upper+1):
    flag=0
    for i in range(2,number):
        if(number%i==0):
            flag=1
            break
    if(flag==0):
            print(number)
