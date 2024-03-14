#Map & filter
# if we need outpt for every element we use map function
# for eg in a lst we need to square every no,in these condition we use map
# lst=[1,2,3,4,5,6,7,8,9,10]===>[1,4,9,16,25,....,100]

#filter function is used when only certains elements are needed in outpt ie,if there is any condition
#for eg in a lst we need only even no we use filter
# lst[1,2,3,4,5,6,7,8,9,10]===>[2,4,6,8,10]

# syntax:
# variable_name=list(map(function,iterable))
# variable_name=list(filter(function,iterable))

#map
lst=[1,2,3,4,5,6,7,8,9,10]
# def square(num):
#     return num**2
# lst1=list(map(square,lst))
#or
# lst1=list(map(lambda num:num**2,lst))
# print(lst1)

#print even no in lst
f=list(filter(lambda num:num%2==0,lst))
print(f)