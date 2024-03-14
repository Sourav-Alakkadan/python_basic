#id,fname,lname,age,course,clgname
#clgname is static ie,constant not changeble
class Student:
    collegename='PNRCLG'
    def reading(self,id,fname,lname,age,course):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.course=course
    def writing(self):
        print(self.id,self.fname,self.lname,self.age,self.course,Student.collegename)
student1=Student()
student1.reading(101,'vinay','k',20,'python')
student1.writing()
student2=Student()
student2.reading(102,'sourav','a',22,'mean')
student2.writing()
student3=Student()
student3.reading(103,'arya','am',21,'bigdata')
student3.writing()
student4=Student()
student4.reading(104,'nandana','m',21,'python')
student4.writing()
student5=Student()
student5.reading(105,'yadhu','raj',25,'mern')
student5.writing()