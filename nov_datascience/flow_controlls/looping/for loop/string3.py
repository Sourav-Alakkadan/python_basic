string='luminartechnolab12345'
count1=0
count2=0
num='0123456789'
for i in string:
    if i in num:
        count1+=1
    else:
        count2+=1
print('Numbers:',count1)
print('Letters:',count2)