#string palindrome
str=input('enter a string:')
rev=str[::-1]
if(str==rev):
    print('string is palindrome')
else:
    print('string is not palindrome')