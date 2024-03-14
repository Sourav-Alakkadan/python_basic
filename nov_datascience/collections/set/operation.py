#Operation
#1.union
#2.intersetion
#3.difference

st1={1,2,3,4,5,6,7,8,9}
st2={6,7,8,9,10,11,12,13,14,15}
#st1 union st2 is{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
st3=st1.union(st2)
print(st3)

#st1 intersection st2 is{6,7,8,9}
st4=st1.intersection(st2)
print(st4)

#difference
#A-B means element present in A not present in B
#st1-st2={1,2,3,4,5}
st5=st1.difference(st2)
print(st5)
#B-A means element present in B not present in A
#st2-st1={10,11,12,13,14,15}
st6=st2.difference(st1)
print(st6)