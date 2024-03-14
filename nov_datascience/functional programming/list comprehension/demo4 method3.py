#method-3:
# syntax:
# lst=[print1 if condition1 else print2 range]-for 2 condition
# lst=[print1 if condition1 else print2 if condition2 else print3 if condition3 else print4 range]

#1 to 50 range even square & odd cube
# lst=[(i,i*i) if i%2==0 else (i,i*i*i) for i in range(1,51)]
# print(lst)

#1 to 50 range
# 1-15   ==>print small
# 16-35  ==>print medium
# 36 more=>print large
lst=[(i,'small') if 1<=i<=15 else (i,'medium') if 15<i<=35 else (i,'large') for i in range(1,51)]
print(lst)
