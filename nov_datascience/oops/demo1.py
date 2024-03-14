# function====>Method(printa and printb)
# self   =====>instance keywords used for create a instance variable
#if create a variable we cannot use it in any other function
# so we can use a instance variable so that it can be used in any other method.
#static  =====>some variable will be constant in every case so we don't need to repeat it
#eg:to collect data of students from a college their clg name will same so we don't need to
# write it in every step so we make it as static variable
class Person:
    def printa(self):
        print('Reading a book')
    def printb(self):
        print('Writing a book')
obj1=Person()
obj1.printa()
obj2=Person()
obj2.printb()
obj2.printa()
obj1.printb()