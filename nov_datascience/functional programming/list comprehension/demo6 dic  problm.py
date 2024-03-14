#key:vehicle
#value:weight
dic={'car':2000,'bike':500,'bus':7000,'cycle':200,'jeep':3000,'suv':4500}
#1.weight above 2000 print vehicle name
lst=[i.upper() for i in dic if dic[i]>2000]
print(lst)
#upper() function is used to convert it into capital letter
#lower() function is used to convert it into small letter