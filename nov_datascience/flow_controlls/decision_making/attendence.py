held=int(input('Enter no.of classes held'))
attended=int(input('Enter no.of classes attended'))
att=(attended/held)*100
print('Class percentage is:',att)
if(att>75):
    print('Student is allowed to sit')
else:
    print('Student is not allowed to sit')