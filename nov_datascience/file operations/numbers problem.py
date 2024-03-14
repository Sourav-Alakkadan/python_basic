#to remove something from python use rstrip() or lstrip() function
#rstrip()-right and lstrip()-left side
#eg:
# data='hello \n'
# data1=data.rstrip('\n')
# print(data1)

#call number file and print it in list and print its sum
f=open('numbers','r')
lst=[]
for i in f:
    lst.append(int(i.rstrip('\n')))    #int is used because it is in string format
print(lst)
print(sum(lst))

