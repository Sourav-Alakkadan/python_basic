# #31.Write a Python program to calculate the area of a circle.
# import math
# radius=float(input('enter radius of circle:'))
# area=math.pi*radius**2
# print('area:',area)


# #32. Create a program that checks if a given number is a perfect square.
# import math
# num=int(input('enter a number:'))
# sqrt_num=math.sqrt(num)
# if sqrt_num.is_integer():
#     print('Number is a perfect square')
# else:
#     print('Number is not a perfect square')


# #33. Write a program to find the square root of a number.
# import math
# num=float(input('Enter a number:'))
# num_sqrt=math.sqrt(num)
# print('Square root is:',num_sqrt)


#34. Create a program that generates a simple to-do list.
# task=[]
# n=int(input('how many no of task:'))
# for i in range(n):
#     t=input('enter your task one by one')
#     task.append(t)
#     if(i==n-1):
#         print('Task over')
#         break
# print(task)



#35. Write a Python program to find the LCM (Least Common Multiple) of two numbers.
# def gcd(a,b):
#     if(a==0):
#         return b
#     return gcd(b%a,a)
# def lcm(a,b):
#     return (a//gcd(a,b))*b
# a=int(input('enter a number:'))
# b=int(input('enter another number:'))
# print('LCM of a,b is:',lcm(a,b))


#36. Create a program to check if a string contains only alphabetic characters.
# str=input('enter a string:')
# flag=0
# for char in str:
#     if not char.isalpha():
#         flag=1
#         break
# if(flag==0):
#     print('string contain only alphabet')
# else:
#     print('string contain alphabet & other')


# #37. Write a program that calculates the power of a number (a^b).
# num=float(input('enter number:'))
# power=int(input('enter power:'))
# res=num**power
# print('Result:',res)


# 38. Create a program to calculate the sum of all natural numbers up to a given N
# n=int(input('enter a number:'))
# sum=0
# for i in range(0,n+1):
#     sum=i+sum
# print(sum)


#39. Write a Python program to find the factorial of a number using a loop.
# num=int(input('Enter a number:'))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)


#40.Create a program to check if a string is a valid email address.
# import re
#
# def valid(email):
#     pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
#     if(re.match(pattern,email)):
#         print('Valid Email')
#     else:
#         print('Invalid Email')
# email=input('Enter a email:')
# valid(email)


#41.Write a program to reverse a list in Python.
# lst=[]
# n=int(input('enter total no of elements:'))
# for i in range(n):
#     num=int(input('enter number:'))
#     lst.append(num)
# print(lst)
# rev=lst[::-1]
# print(rev)


#42.Create a program to check if a given number is a palindrome.
# num=input('Enter a number: ')
# if(num==num[::-1]):
#     print('Number is palindrome')
# else:
#     print('Number is not palindrome')


#43.. Create a program to check if a given number is a palindrome.
# para=input('enter a paragraph')
# dic={}
# data=para.split(' ')
# for i in data:
#     if i not in dic:
#         dic[i]=1
#     else:
#         dic[i]+=1
# print(dic)


#44. Create a program to find and print the Fibonacci sequence up to N terms.
# n=int(input('Enter total no of elements'))
# num1=0
# num2=1
# for i in range(n):
#     temp=num1
#     num1=num2
#     num2=num2+temp
#     print(temp)


#45. Write a program to check if a list is sorted in ascending order.
# lst=[]
# for i in range(5):
#     num=int(input('enter numbers:'))
#     lst.append(num)
# lst1=lst[:]
# lst1.sort()
# if(lst==lst1):
#     print("The list is sorted in ascending order")
# else:
#     print('The list is not sorted in ascending order')


#46. Create a program that calculates the area of a triangle.
# base=int(input('enter base length of triangle'))
# height=int(input('enter height of triangle'))
# area=(base*height)/2
# print('Area is:',area)



#47.Write a Python program to find the GCD (Greatest Common Divisor) of two numbers.
# num1=int(input('Enter a number:'))
# num2=int(input('Enter another number:'))
# min=min(num1,num2)
# gcd=1
# for i in range(1,min+1):
#     if(num1%i==0)&(num2%i==0):
#         gcd=i
# print("GCD is:",gcd)


#48.Create a program to print the ASCII value of a character.
# char=input('enter the character')
# print(ord(char))


#49.Write a program to find and print all prime numbers up to N.
# n=int(input('enter total no of elements'))
# for number in range(2,n+1):
#     flag=0
#     for i in range(2,number):
#         if(number%i==0):
#             flag=1
#     if(flag==0):
#         print(number)


#50.Create a program that converts a decimal number to binary.
# decimal=int(input('enter a number:'))
# b=''
# while decimal>0:
#     r=decimal%2
#     b=str(r)+b
#     decimal//=2
# print('binary is:',b)


#51.Write a Python program to find the minimum and maximum elements in a list.
# lst=[]
# for i in range(10):
#     num=int(input('enter list numbers:'))
#     lst.append(num)
# print(min(lst))
# print(max(lst))


#52.Create a program to count the number of uppercase and lowercase letters in a string
# str=input('enter a string')
# uc=0
# lc=0
# for char in str:
#     if(char.isupper()):
#         uc+=1
#     elif(char.islower()):
#         lc+=1
# print('no.of uppercase:',uc)
# print('no.of lowercase:',lc)


#53.Write a program to reverse the order of words in a sentence.
# str=input('Enter a sentence:')
# word=str.split(' ')
# rev=word[::-1]
# rev_str=' '.join(rev)
# print('Reversed sentence:',rev_str)


# 54. Create a program to calculate the sum of a geometric series.
# a=float(input('enter 1st number:'))
# r=float(input("enter common ratio:"))
# n=int(input('enter total no of elements:'))
# sum=(a*(1-a**n))/(1-n)
# if r==1:
#     print('sum geometric series is:',a*n)
# else:
#     print("sum geometric series is:",sum)


#55. Write a Python program to calculate the volume of a sphere
# import math
# r=float(input('enter radius of sphere:'))
# vol=(4*(math.pi*r**3))/3
# print('Volume of sphere:',vol)


#56.Create a program that generates a random password of a given length
# import random
# import string
# length=int(input("enter length of password:"))
# char=string.ascii_letters+string.digits + string.punctuation
# password=''
# for i in range(length):
#     password+=random.choice(char)
# print(password)


#57.Write a program to find and print the factors of a number.
# num=int(input('enter a  number:'))
# fact=[]
# for i in range(1,num+1):
#     if(num%i==0):
#         fact.append(i)
# print(fact)


#58. Create a program to check if a list contains duplicate elements.
# lst=[]
# for i in range(10):
#     num=int(input('enter number:'))
#     lst.append(num)
# lst.sort()
# flag=0
# for i in range(1,len(lst)):
#     for j in range(0,i):
#         if(lst[i]==lst[j]):
#             flag=1
# if(flag==0):
#     print('It has no duplicate values:')
# else:
#     print('it has duplicate values')


#59. Write a Python program to find and replace a word in a string.
# str=input('enter a string:')
# word=input('enter word to find:')
# replace=input('enter word to replace:')
# str2=str.replace(word,replace)
# print(str2)


#60.Create a program that checks if a given string is a pangram (contains all alphabets).
# str=input('enter a string:')
# for i in str:
#     if(i.isalpha()):
#         flag=1
#     else:
#         flag=0
# if(flag==1):
#     print("contains only alphabets")
# else:
#     print('contains other than alphabet')
