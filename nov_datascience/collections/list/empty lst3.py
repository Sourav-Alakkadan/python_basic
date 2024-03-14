#create a list from 1 to 100
#even no to 1 list
#odd no to other lst
#find list sum,odd lst sum,even lst sum
lst=[]
evlst=[]
odlst=[]
for i in range(1,101):
    lst.append(i)
print(lst)
for i in lst:
    if(i%2==0):
        evlst.append(i)
    else:
        odlst.append(i)
print(evlst)
print(odlst)
print(sum(lst))
print(sum(evlst))
print(sum(odlst))
