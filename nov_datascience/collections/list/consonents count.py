string='luminartechnolab'
vowel='aeiou'
lst=[]
for i in string:
    if i not in vowel:
        lst.append(i)
print(len(lst))