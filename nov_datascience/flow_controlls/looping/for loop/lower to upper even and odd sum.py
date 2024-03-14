lower=int(input('Enter lower limit:'))
upper=int(input('Enter upper limit:'))
odd_sum=0
even_sum=0
for i in range(lower,upper+1):
    if(i%2==0):
        even_sum+=i
    else:
        odd_sum+=i
print("Even sum=",even_sum)
print('Odd sum=',odd_sum)