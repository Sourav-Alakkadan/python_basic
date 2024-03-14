#word count(no.of word in a sentence)
line='cat rat bat hello cat rat bat hello cat'
#cat=3
#rat=2
#bat=2
#hello=2

#1st we need to split the data word by word
#to split we use split()
data=line.split(' ')
#print(data)
dic={}
for i in data:         #i=cat   i=rat
    if(i not in dic):  #
        dic[i]=1       #dic[cat]=1   dic[rat]=1
    else:
        dic[i]+=1
print(dic)