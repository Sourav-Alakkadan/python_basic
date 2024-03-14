#list slicing
lst=[1,5,4,12,8,6,22,15,55,14,9,3,40]
#lst[start:stop(stop-1)]
print(lst[2:7])  #index=2 to 6
print(lst[4:10]) #index=4 to 9
print(lst[1:])   #index=1 to end of the list
print(lst[:6])   #index=0 to 5
print(lst[2:10:2])#index=2 to 10 with i+=2 iteration ie,index=2,4,6,8
print(lst[3:11:2])

#positive indexing ===> left to right[0 to n-1]
#negative indexing ===> right to left[n-1 to 0]
print(lst[-2])
print(lst[-7])