#create a simple calculator using function

def cal():
    num1=int(input('Enter 1st number :'))
    num2=int(input('Enter 2nd number :'))
    print('Press 1 for addition :\n'
          'Press 2 for subtraction :\n'
          'Press 3 for multiplication :\n'
          'Press 4 for division :')
    value=int(input('Choose your selection :'))
    if(value==1):
        sum=num1+num2
        print('Result=', sum)
    elif(value==2):
        sum=num1-num2
        print('Result=', sum)
    elif(value==3):
        sum=num1*num2
        print('Result=', sum)
    elif(value==4):
        sum=num1/num2
        print('Result=', sum)
    else:
        print('Invalid selection')
cal()
