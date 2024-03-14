#print 1st recursive character(repeating character)
pattern='ABCDFBCDFSDFGH'
dic={}
for i in pattern:
    if(i not in dic):
        dic[i]=1
    else:
        print('1st Recursive character is:',i)
        break