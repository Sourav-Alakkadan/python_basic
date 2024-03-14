st={10,20,30,15,25}
#add one element to a set
#use add() funtion
# st.add(90)
# st.add(60)
#print(st)

#to add multiple values to a set
#use update() funtion
# st.update([40,50,55])
# print(st)

#how to delete a element
#use remove() and discard() funtion
# st.remove(10)
# st.remove(50)
# print(st)
#only single element can be removed
#diff b/w remove and discard
st.remove(100)
print(st) #it has return type

st.discard(100)
print(st) #it has no return type