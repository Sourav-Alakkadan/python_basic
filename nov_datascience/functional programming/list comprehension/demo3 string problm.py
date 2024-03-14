#vowels count
string='luminartechnolab'
vowels='aeiouAEIOU'
# lst=[i for i in string if i in vowels]          #or lst=len([i for i in string if i in vowels])
# print(len(lst))                                     print(lst)

#consonents
lst=[i for i in string if i not in vowels]
print(len(lst))