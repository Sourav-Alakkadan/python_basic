#1 to 1000
#1.find all of the no from 1-1000 div by 8
# lst=[i for i in range (1,1001) if i%8==0]
# print(lst)

#2.find all of the no from 1-1000 that have 6 in them
# a='6'
# lst=[i for i in range(1,1001) if a in str(i)]
# print(lst)

#3.count no.of spaces in the string
string='practice problems to drill list comprehension in your head'
# lst=len([i for i in string if i==' '])
# print(lst)

#4.count no.of vowels in the string
# vowels='aeiouAEIOU'
# lst=len([i for i  in string if i in vowels])
# print(lst)

#5.find all of the words in the string that are less than 5 letters
data=string.split(' ')
lst=[i for i in data if len(i)<5]
print(lst)