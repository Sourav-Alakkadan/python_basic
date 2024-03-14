#Constructor
#if we use constuctor we can assign values we can object is created
#ie,method will be replaced by constructor
#benfits:

# class A:
#     def B(self,id,fname,lname):
#         self.id=id
#         self.fname=fname
#         self.lname=lname
#     def C(self):
#         print(self.id,self.fname,self.lname)
# a1=A()
# a1.B(101,'vinay','a')
#

class Person:
    def __init__(self,id,fname,lname,age):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age)
person1=Person(101,'vinay','a',27)
person1.printvalue()
person2=Person(102,'sourav','raj',21)
person2.printvalue()