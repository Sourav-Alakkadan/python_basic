#List comprehension
#there are many problems in list so to reduse it into single line we use list comprehension

# Method:
# 1.Range of element added into a list
# 2.Range of elements added into a list based on one condition
# 3.Range of elements added into a list based on more than one condition


#method 1:
#syntax:
#lst=[print range]
# eg-1:print 1 to 30
# lst=[i for i in range(1,31)]
# print(lst)

#2:print 1 to 25
# lst=[i for i in range(1,26)]
# print(lst)

#3: 1 to 10 range square
# lst=[i*i for i in range(1,11)]
# print(lst)

#4: add 5 with every elements in the list
lst=[1,2,3,4,5]
lst1=[i+5 for i in lst]
print(lst1)
