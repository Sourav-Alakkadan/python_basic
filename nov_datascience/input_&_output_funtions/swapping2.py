#swapping without temp variable
num1=10
num2=20
print('Before swapping')
print('Number1 is',num1)
print('Number2 is',num2)

num1=num1+num2   #10+20=30
num2=num1-num2   #30-20=10
num1=num1-num2   #30-10=20
print('After swapping')
print('Number1 is',num1)
print('Number2 is',num2)