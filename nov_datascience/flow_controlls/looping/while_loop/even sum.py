lower=int(input('Enter lower limit:'))
upper=int(input('Enter upper limit:'))
sum=0
while(lower<=upper):
    if(lower%2==0):
        sum=lower+sum
    lower+=1
print('Total=',sum)
