#find word count in the file words
f=open('words','r')
dic={}
for i in f:
    data=i.rstrip('\n').split(' ')
    # print(data)
    for j in data:
        if j not in dic:
            dic[j]=1
        else:
            dic[j]+=1
# print(dic)
for k,v in dic.items():     #k,v is used to print downwards with key and value seperately
    print(k,'','',v)