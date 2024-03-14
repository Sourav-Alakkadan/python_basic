dic={'id':101,'fname':'Vinay','lname':'k','age':28,'prof':'bigdata'}
# print(dic)
#to collect particular value we use key name
#ie,to print vinay we use key fname
# print(dic['fname'])
# print(dic['age'])

for i in dic:             #here i represent key
    print(i,dic[i])       #to print both key and value use for loop

#to change value
dic['age']=50   #or dic['age']+=22
print(dic)

#to add new key value pair
dic['marks']=70
print(dic)

#to delete a key value pair
del dic['id']
print(dic)

#to check values in dic
print('age' in dic)
print('salary' in dic)
print('fname' not in dic)