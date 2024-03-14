class Person:
    def setvalue(self,fname,lname,age,prof,location):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof
        self.location=location
    def printvalue(self):
        print(self.fname,self.lname,self.age,self.prof,self.location)
person1=Person()
person1.setvalue('vinay','k',29,'bigdata','ernakulam')
person1.printvalue()
person2=Person()
person2.setvalue('rahul','m',30,'python','calicut')
person2.printvalue()
person3=Person()
person3.setvalue('jithin','tp',22,'django','kannur')
person3.printvalue()
person4=Person()
person4.setvalue('sourav','a',25,'mean','kollam')
person4.printvalue()
person5=Person()
person5.setvalue('arya','sm',27,'data science','kottayam')
person5.printvalue()