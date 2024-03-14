#write the multiplication table of a given number
#num
#1*num=ans
#2*num=ans
num=int(input('Enter a number'))
i=1
while(i<=10):
    sum=num*i
    print(i,'*',num,'=',sum)
    i+=1