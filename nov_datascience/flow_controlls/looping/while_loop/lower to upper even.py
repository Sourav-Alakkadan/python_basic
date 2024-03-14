#print lower to upper limit even number

lower=int(input('Enter lower limit:'))
upper=int(input('Enter upper limit:'))
while(lower<=upper):
    if(lower%2==0):
        print(lower)
    lower+=1
