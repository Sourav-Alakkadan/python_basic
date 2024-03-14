lower=int(input('Enter lower limit:'))
upper=int(input('Enter upper limit:'))
even_sum=0
odd_sum=0
while(lower<=upper):
    if(lower%2==0):
        even_sum=even_sum+lower

    else:
        odd_sum=odd_sum+lower
    lower+=1
print('Total even sum =',even_sum)
print('Total odd sum =', odd_sum)
