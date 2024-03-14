#find the factorial using function

#1.
# def fact():
#     num=int(input('Enter a number:'))
#     fac=1
#     for i in range(1,num+1):
#         fac=fac*i
#     print(fac)
# fact()

#2.
#
# def fact(num):
#     f=1
#     for i in range(1,num+1):
#         f=f*i
#     print(f)
# fact(5)

#3.
def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f
result=fact(5)
print(result)
