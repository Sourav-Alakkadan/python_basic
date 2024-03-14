# 1. Write a Python program to print "Hello, World!" to the screen
# print('"Hello, World!"')
#
# 2. Write a program to take user input (their name) and display it on the screen.
# name=input('Enter your name:')
# print(name)


#3. Create a Python program to calculate the sum of two numbers.
# num1=int(input('enter number 1:'))
# num2=int(input('enter number 2:'))
# sum=num1+num2
# print(sum)

# 4. Write a program to check if a number is even or odd.
# num=int(input('enter a number:'))
# if(num%2==0):
#     print('Number is even')
# else:
#     print('Number is odd')

#5. Create a program that calculates the square of a number.
# num=int(input('Enter a number:'))
# sum=num*num
# print('Square is:',sum)

# 6. Write a Python program to find the maximum of two numbers.
# num1=int(input('enter number 1:'))
# num2=int(input('enter number 2:'))
# print(max(num1,num2))

# 7. Write a program that prints the numbers from 1 to 10.
# for i in range(1,11):
#     print(i)

#8. Create a Python program to print the multiplication table of a given number
# num=int(input('enter a number'))
# for i in range(1,11):
#     sum=i*num
#     print(i,'*',num,'=',sum)

# 9. Write a program to check if a given number is positive, negative, or zero
# num=int(input('Enter a number:'))
# if(num<0):
#     print('Number is negative')
# elif(num>0):
#     print('Number is positive')
# else:
#     print('Number is zero')

#10. Create a program that calculates the factorial of a number.
# num=int(input('Enter a number:'))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)

#11. Write a Python program to check if a number is prime.
# num=int(input('enter a number:'))
# flag=0
# for i in range(2,num):
#     if(num%i==0):
#         flag=1
# if(flag==0):
#     print('Number is prime')
# else:
#     print('Number is not prime')

#12. Create a program to swap the values of two variables.
# a=int(input('enter a number'))
# b=int(input('enter another number'))
# a=a+b
# b=a-b
# a=a-b
# print('swapped values')
# print(a)
# print(b)

#13. Write a program to calculate the average of a list of numbers.
# lst=[]
# n=int(input('Enter no of  element:'))
# for i in range(n):
#     num1=int(input('Enter element for lst:'))
#     lst.append(num1)
# print(lst)
# len=len(lst)
# avg=sum(lst)/len
# print(avg)

#14. Create a program that finds the largest number in a list.
# lst=[]
# n=int(input('Enter no of  element:'))
# for i in range(n):
#     num1=int(input('Enter element for lst:'))
#     lst.append(num1)
# print(lst)
# num=lst[0]
# for i in lst[1:]:
#     if num<i:
#         num=i
# print('largest is ',num)

#15. Write a Python program to reverse a string.
# str=input('enter a string')
# rev=str[::-1]
# print(rev)

#16.Write a Python program to find the length of a string
# str=input('Enter string:')
# length=0
# for char in str:
#     length+=1
# print(length)

#17. Write a program to check if a string is a palindrome.
# str=input('enter a string')
# str1=str.lower()
# rev=str1[::-1]
# if(rev==str1):
#     print('string is palindrome')
# else:
#     print('String is not palindrome')

#18. Create a program to count the number of vowels in a string.
# str=input('enter a string')
# vowels='aeiouAEIOU'
# count=0
# for i in str:
#     if i in vowels:
#         count+=1
# print(count)

# 19. Write a Python program to find the sum of all even numbers from 1 to 100
# sum=0
# for i in range(1,101):
#     if(i%2==0):
#         sum+=i
# print(sum)

# 20. Create a program to check if a given year is a leap year.
# year=int(input('enter year:'))
# if(year%4==0)&(year%100!=0)or(year%400==0):
#     print('year is a leap year')
# else:
#     print('not a leap year')

# 21. Write a program that generates a random number and asks the user to guess it.
# import random
# num=random.randint(1,100)
# print('Guess a number between 1 to 100\n you have 3 guesses')
# for i in range(3):
#     guess=int(input('enter your guess'))
#     if (guess==num):
#         print('your guess is correct')
#     else:
#         print('your guess is wrong')
#         if(i==2):
#             print('Sorry out off guesses!!\n the number was',num)

#22. Create a program that converts Fahrenheit to Celsius.
# faren=float(input('enter temperature in farenheat:'))
# celsius=(5/9)*(faren-32)
# print('Temperature in celsius is:',celsius)

#23. Write a Python program to calculate the area of a rectangle.
# l=int(input('Enter length'))
# b=int(input('Enter breadth'))
# area=l*b
# print('Area of the rectangle',area)

#24. Create a program that counts the number of words in a sentence.
# line=input('enter a string')
# data=line.split(' ')
# dic={}
# for i in data:
#     if i not in dic:
#         dic[i]=1
#     else:
#         dic[i]+=1
# print(dic)

#25. Write a program to find the common elements between two lists.
# lst1=[]
# lst2=[]
# n=int(input('Enter no of  element:'))
# for i in range(n):
#     num1=int(input('Enter element for lst1:'))
#     lst1.append(num1)
# print(lst1)
# for i in range(n):
#     num2=int(input('Enter element for lst2:'))
#     lst2.append(num2)
# print(lst2)
# print('common element is')
# for i in lst1:
#     for j in lst2:
#         if(i==j):
#             print(i)

#26. Create a program that sorts a list of numbers in ascending order.
# lst=[]
# n=int(input('Enter no of elements:'))
# for i in range(n):
#     num=int(input('enter numbers:'))
#     lst.append(num)
# print(lst)
# print('sorted list :')
# lst.sort()
# print(lst)

#27.Write a Python program to find the second largest element in a list
# lst=[]
# n=int(input('Enter no of elements:'))
# for i in range(n):
#     num=int(input('enter numbers:'))
#     lst.append(num)
# print(lst)
# l=max(lst)
# lst.remove(l)
# sl=max(lst)
# print('Second largest:',sl)

#28. Create a program that generates a simple calculator
# num1=int(input('Enter 1st number:'))
# num2=int(input('Enter 2nd number:'))
# value=int(input('Press :\n 1 for addition\n 2 for subtraction\n 3 for multiplication\n 4 for division\n '
#             'Please enter your choice:'))
# if(value==1):
#     res=num1+num2
# elif(value==2):
#     res=num1-num2
# elif(value==3):
#     res=num1*num2
# elif(value==4):
#     res=num1/num2
# else:
#     print('Wrong choice')
# print('Result:',res)

#29. Write a program to check if a given string contains only digits.
# str=input('enter a string')
# for i in str:
#     if(i.isdigit()):
#         flag=0
#     else:
#         flag=1
# if(flag==0):
#     print('String has digit')
# else:
#     print('String does not have digit')

#30.Create a program to calculate the sum of all prime numbers from 1 to 100
# sum=0
# for i in range(1,101):
#     flag=0
#     for j in range(2,i):
#         if(i%j==0):
#             flag=1
#             break
#     if(flag==0):
#         sum=sum+i
# print(sum)
