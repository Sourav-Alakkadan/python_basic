#grade
sub1=int(input('Enter your mark for subject1:'))
sub2=int(input('Enter your mark for subject2:'))
sub3=int(input('Enter your mark for subject3:'))
sub4=int(input('Enter your mark for subject4:'))
total=(sub1+sub2+sub3+sub4)
print('Total:',total)
if(total>=180):
    print('A+')
elif(160<=total<=179):
    print('A')
elif(140<=total<=159):
    print('B+')
elif(120<=total<=139):
    print('B')
elif(100<=total<=119):
    print('C+')
elif(80<=total<=99):
    print('C')
else:
    print('Failed')