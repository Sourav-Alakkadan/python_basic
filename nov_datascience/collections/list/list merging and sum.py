#merging of list and addition

lst1=[]
limit=int(input('enter list limit:'))
for i in range(limit):
    num=int(input('enter list elements:'))
    lst1.append(num)
print(lst1)
lst2=[]
for i in range(limit):
    num2=int(input('enter list elements:'))
    lst2.append(num2)
print(lst2)
lst3=lst1+lst2            #mergeing of 2 list into 3rd
print('Merged list:',lst3)
lst4=[]
for i in range(limit):
    sum=lst1[i]+lst2[i]   #addition of 2 list into 3rd
    lst4.append(sum)
print('Sum :',lst4)