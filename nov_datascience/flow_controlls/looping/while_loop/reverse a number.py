#Reverse a number
num=int(input('Enter a number:'))   #456
rev=0
while(num!=0):        #456!=0
    last=num%10       #6=456%10...6
    rev=(rev*10)+last #0=(0*10)+6...6
    num//=10          #456//=10...45
print(rev)
