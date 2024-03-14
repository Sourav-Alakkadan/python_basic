# method-2:
# syntax:
# lst=[print range if condition]
# eg-1: 1 to 20 even no
# lst=[i for i in range(1,21) if i%2==0]
# print(lst)

#2: 1 to 30 div by 5
# lst=[i for i in range(1,31) if i%5==0]
# print(lst)

#3: 1 to 40 range odd no square
lst=[(i,i*i) for i in range(1,41) if i%2==1]
print(lst)

