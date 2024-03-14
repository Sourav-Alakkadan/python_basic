f=open('C:/Users/soura/Downloads/Telegram Desktop/txn (1).txt','r')
# 1:row count
count=0
for i in f:
    count+=1
print('Row count:',count)

# 2:jan month
# count=0
# for i in f:
#     data=i.rstrip('\n').split(',')
#     date=data[1].split('-')
#     month=date[0]
#     if month=='01':
#         count+=1
#         print(data[0:5:2],data[5:8:2])
#         print(count)

# 3:july month
# count=0
# for i in f:
#     data=i.rstrip('\n').split(',')
#     date=data[1].split('-')
#     month=date[0]
#     if month=='07':
#         count+=1
#         print(data[0:5:2],data[5:8:2])
#         print(count)

# 4:category count
# dic={}
# for i in f:
#     data=i.rstrip('\n').split(',')
#     cat=data[4]
#     if cat not in dic:
#         dic[cat]=1
#     else:
#         dic[cat]+=1
# for k,v in dic.items():
#     print(k,'','',v)
# des=sorted(dic.values(),reverse=True)
# print(des)

# 5:cat full details


# 6:payment count
# dic={}
# for i in f:
#     data=i.rstrip('\n').split(',')
#     payment=data[8]
#     if payment not in dic:
#         dic[payment]=1
#     else:
#         dic[payment]+=1
# for k,v in dic.items():
#     print(k,'','',v)

# 7:jan-july purchase count
# count=0
# for i in f:
#     data=i.rstrip('\n').split(',')
#     date=data[1].split('-')
#     month=date[0]
#     if '01'<=month<='07':
#         count+=1
# print('Jan-July purchase count:',count)

#8:each cat total amount
# dic={}
# for i in f:
#     data=i.rstrip('\n').split(',')
#     cat=data[4]
#     amt=float(data[3])
#     if cat not in dic:
#         dic[cat]=amt
#     else:
#         dic[cat]+=amt
# for k,v in dic.items():
#     print(k,'','',v)

# 9:each cat max amount
# dic={}
# for i in f:
#     data=i.rstrip('\n').split(',')
#     cat=data[4]
#     amt=float(data[3])
#     if cat in dic:
#         if amt>=dic[cat]:
#             dic[cat]=amt
#     else:
#         dic[cat]=amt
# for k,v in dic.items():
#     print(k,'','',v)

# 10:each cat avg amt
# dic_amt={}
# dic_count={}
# for i in f:
#     data=i.rstrip('\n').split(',')
#     cat=data[4]
#     amt=float(data[3])
#     if cat in dic_amt:
#         dic_amt[cat]+=amt
#         dic_count[cat]+=1
#     else:
#         dic_amt[cat]=amt
#         dic_count[cat]=1
# for i in dic_amt:
#     cat_avg=(dic_amt[i]/dic_count[i])
#     print(i,cat_avg)

# 11:total amt by cash & credit
# dic={}
# for i in f:
#     data=i.rstrip('\n').split(',')
#     pay=data[8]
#     amt=float(data[3])
#     if pay in dic:
#         dic[pay]+=amt
#     else:
#         dic[pay]=amt
# print(dic)

# 12:indoor games total amt
# dic={}
# for i in f:
#     data=i.rstrip('\n').split(',')
#     ind_games=data[4]
#     amt=float(data[3])
#     if ind_games=='Indoor Games':
#         if ind_games in dic:
#             dic[ind_games]+=amt
#         else:
#             dic[ind_games]=amt
# print(dic)

# 13:each state count
# dic={}
# for i in f:
#     data=i.strip('\n').split(',')
#     state=data[-2]
#     if state not in dic:
#         dic[state]=1
#     else:
#         dic[state]+=1
# print(dic)