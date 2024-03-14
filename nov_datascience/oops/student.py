#id,fname,lname,age,course,location
class Student:
    def reading(self,id,fname,lname,age,course,location):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.course=course
        self.location=location
    def writing(self):
        print(self.id,self.fname,self.lname,self.age,self.course,self.location)
student1=Student()
student1.reading(101,'vinay','k',20,'python','kannur')
student1.writing()
student2=Student()
student2.reading(102,'sourav','a',22,'mean','kollam')
student2.writing()
student3=Student()
student3.reading(103,'arya','am',21,'bigdata','kottayam')
student3.writing()
student4=Student()
student4.reading(104,'nandana','m',21,'python','kasargod')
student4.writing()
student5=Student()
student5.reading(105,'yadhu','raj',25,'mern','thrissur')
student5.writing()
