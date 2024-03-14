salary=int(input('Enter your salary:'))
service=int(input('Enter your year of service:'))
if(service>=5):
    bonus=(salary*5)/100
    print('Bonus is :',bonus)
else:
    print('Not eligible for bonus')