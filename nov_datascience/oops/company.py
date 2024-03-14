#id,fname,lname,age,prof,companyname
#5 employee
#prof & com name static
class Company:
    prof='Engineer'
    companyname='TATA'
    def setvalue(self,id,fname,lname,age):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,Company.prof,Company.companyname)
company1=Company()
company1.setvalue(101,'vinay','k',35)
company1.printvalue()
company2=Company()
company2.setvalue(102,'amal','a',30)
company2.printvalue()
company3=Company()
company3.setvalue(103,'arya','kv',37)
company3.printvalue()
company4=Company()
company4.setvalue(104,'jithin','a',40)
company4.printvalue()
company5=Company()
company5.setvalue(105,'akhil','mv',32)
company5.printvalue()