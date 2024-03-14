lower=int(input('Enter lower limit:'))
upper=int(input('Enter upper limit:'))
for i in range(lower,upper+1):
    if(i%5==0):
        print(i)