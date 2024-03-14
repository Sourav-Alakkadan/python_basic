price=int(input('Enter your bike price'))
if(price>100000):
    tax=(price*15)/100
    print('Tax is:',tax)
elif(price>=50000)&(price<=100000):
    tax=(price*10)/100
    print('Tax is:',tax)
else:
    tax=(price*5)/100
    print('Tax is:',tax)