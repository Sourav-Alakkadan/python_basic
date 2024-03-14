#electricity bill

units=int(input('Enter electricity unit consumed:'))
if(101<=units<=200):
    bill=(units-100)*5
    print('Current bill:',bill)
elif(units>200):
    bill=(100*5)+(units-200)*10
    print('Current bill:',bill)
else:
    print('No charge')

