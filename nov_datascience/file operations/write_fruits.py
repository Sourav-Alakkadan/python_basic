f=open('write_fruits', 'r')
f1=open('write_fruits1','w')
for i in f:
    if i!='apple\n':   #or if i not in 'apple':
        f1.write(i)