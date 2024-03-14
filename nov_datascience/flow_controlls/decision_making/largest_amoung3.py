#Largest amoung 3 numbers
num1=int(input('Enter 1st number'))
num2=int(input('Enter 2nd number'))
num3=int(input('Enter 3rd number'))
if(num1>num2)&(num1>num3):
    print('First number is greatest')
elif(num2>num1)&(num2>num3):
    print('Second number is largest')
else:
    print('Third number is largest')